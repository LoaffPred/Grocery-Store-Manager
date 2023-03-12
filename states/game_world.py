from states.state import State
from states.price_change import PriceChange
from states.market import Market
from states.monthlydues import MonthlyDue
import random
from decorators import *
from beautifultable import BeautifulTable
from util import *


class GameWorld(State):
    """GameWorld class - handles all events and properties of the main game simulation.
    Simulates various customer purchases and updating the interface"""

    def __init__(self, game, name, data):
        super().__init__(game)
        self.game.player.name = name
        self.game.player.load_player_data(data)
        self.market_stockpile = read_json("baseStockpile.json")
        self.worldtable = self.create_worldtable()
        self.actions = "[1] Simulate\n[2] Restock\n[3] Change Prices\n[0] Save and Exit"

    @print_header("GAME WORLD SIMULATION")
    def update(self):
        """Runs and updates logic and events of the game world simulation"""
        self.update_worldtable()
        self.game.update_interface(self.worldtable, options=self.actions)
        self.game.print_interface()
        self.render()
        choice = self.game.get_input()
        # ======================== Simulate ======================== #
        if choice == "1":
            print(">>> Simulate <<<")
            self.buy()
            self.game.player.days_played += 1
            # MonthlyDues state runs after every month/28 days
            if self.game.player.days_played % 28 == 0:
                new_state = MonthlyDue(self.game)
                new_state.enter_state()
        # ========================  Restock ======================== #
        elif choice == "2":
            new_state = Market(self, self.game)
            new_state.enter_state()
        # ======================== Change Prices ======================== #
        elif choice == "3":
            new_state = PriceChange(self.game)
            new_state.enter_state()
        # ======================== Save and Exit ======================== #
        elif choice == "0":
            self.game.player.save_player_data()
            self.exit_state()

    def render(self):
        """Prints additional information regarding player status"""
        print("Day", self.game.player.days_played)
        print("Your balance: \u20B1", self.game.player.balance)

    def create_worldtable(self):
        """Creates table for game simulation interface"""
        table = BeautifulTable()
        table.columns.header = ["PLAYER"]
        table.rows.append(["Player Stockpile"])
        table = self.game.format_table(table)

        return table

    def create_playertable(self, stockpile):
        """Creates table for player stockpile information"""
        table = BeautifulTable()
        table.columns.header = ["Item", "Quantity", "Price"]
        for k, v in stockpile.items():
            table.rows.append([k, v["quantity"], "\u20B1 " + str(v["price"])])

        table = self.game.format_table(table)
        table.columns.header.alignment = BeautifulTable.ALIGN_CENTER
        table.columns.alignment["Price"] = BeautifulTable.ALIGN_LEFT

        return table

    def update_worldtable(self):
        """Inserts player table into world table"""
        self.worldtable.rows[0][0] = self.create_playertable(self.game.player.stockpile)

    @transition_pause
    def buy(self):
        """Simulates a customer choosing what to buy via random selection,
        and whether the prices are desirable.
        Randomly selects categories, items from those categories,
        and how many of those items [if 0, then no transaction].
        Calculates and returns the weighted total of all the items bought.
        """

        print("====>>> Simulation summary for the day <<<====")
        total_amount = 0
        # Gets random selection of produce items
        items = random.sample(
            list(self.game.player.stockpile.keys()),
            k=random.randint(0, len(self.game.player.stockpile.keys())),
        )
        # Loops through every produce item and decides whether to buy or not and how many
        for item in items:
            item_desirability = self.is_desirable(
                self.game.player.stockpile[item]["price"],
                self.market_stockpile[item]["price"],
            )
            if item_desirability:
                try:
                    quantity = random.randint(
                        1, 5 % (self.game.player.stockpile[item]["quantity"] + 1)
                    )
                    self.game.player.stockpile[item]["quantity"] -= quantity
                    total_item_price = (
                        quantity * self.game.player.stockpile[item]["price"]
                    )
                    total_amount += total_item_price

                    summary = "Customers bought {} {}, worth \u20B1 {}".format(
                        quantity, item, total_item_price
                    )
                    print(summary)
                except ValueError or ZeroDivisionError:
                    continue

                self.game.player.balance += total_amount

    def is_desirable(self, price, srp):
        """Determines if the price of an item is desirable or not;
        Used in [buy()] function"""
        if price < srp:
            return True
        elif price <= srp + 10:
            return random.choice([True, False])
        else:
            return False
