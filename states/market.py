from states.state import State
from util import *
import random
from decorators import *
from beautifultable import BeautifulTable


class Market(State):
    """Market class - handles all events and properties of the market
    Simulates inflation, deflation, and varied market supply"""

    def __init__(self, game_world, game):
        super().__init__(game)
        self.game_world = game_world
        self.stockpile = read_json("baseStockpile.json")
        self.inflation()
        self.random_supply()
        self.create_markettable()
        self.game_world.worldtable.columns.append([""], header="MARKET")

    @print_header("MARKET")
    def update(self):
        """Runs and updates logic and events of the market"""
        # Updates all interfaces
        self.update_markettable()
        self.game_world.update_worldtable()
        self.game.update_interface(
            self.game_world.worldtable, options="[1] Buy From Market\n[0] Go Back"
        )
        self.game.print_interface()
        choice = self.game.get_input()
        # ======================== Buy From Market ======================== #
        if choice == "1":
            self.sell()
        # ========================  Go Back ======================== #
        elif choice == "0":
            # Updates interface by deleting previous market table
            del self.game_world.worldtable.columns["MARKET"]
            self.game.player.days_played += 1
            self.exit_state()

    def create_markettable(self):
        """Creates table for market interface"""
        table = BeautifulTable()
        table.columns.header = ["Item", "Quantity", "Price"]
        for k, v in self.stockpile.items():
            table.rows.append([k, v["quantity"], "\u20B1 " + str(v["price"])])

        table = self.game.format_table(table)
        table.columns.header.alignment = BeautifulTable.ALIGN_CENTER
        table.columns.alignment["Price"] = BeautifulTable.ALIGN_LEFT

        return table

    def update_markettable(self):
        """Inserts market table into world table"""
        self.game_world.worldtable.columns["MARKET"] = [self.create_markettable()]

    @transition_pause
    def sell(self):
        """Gets an item and quantity from user and updates both player's
        and market's stockpiles simulating a transaction. Cannot sell
        more than what the market has, and more than what the player can afford.
        """

        print("Enter produce name to buy: [Case-sensitive]")
        choice = input(">>> ")
        if choice in self.stockpile.keys():
            print("Your balance: \u20B1", self.game.player.balance)
            print("Enter quantity of {} to buy:".format(choice))
            num = self.get_input()
            if num:
                total_amount = num * self.stockpile[choice]["price"]
                if num > self.stockpile[choice]["quantity"]:
                    print(
                        "Buy less than or equal to what the market has...".format(
                            choice
                        )
                    )
                elif self.game.player.balance < total_amount:
                    print("You don't have enough money to buy that...")
                else:
                    self.game.player.stockpile[choice]["quantity"] += num
                    self.stockpile[choice]["quantity"] -= num
                    self.game.player.balance -= total_amount
                    print("Purchase successful.")
        else:
            print("Produce not found in stockpile.")

    @num_only
    def get_input(self):
        """Used as target function for decorator"""
        num = input(">>> ")
        return num

    def inflation(self):
        """Simulates change in market produce prices.
        Both price increase and decrease"""

        # k -> how many items' prices to modify
        items = random.sample(list(self.stockpile.keys()), k=random.randint(3, 7))
        for item in items:
            option = random.choice(["inflate", "deflate"])
            # change this value to modify the weight of the change
            # same as a% to b%
            weight = random.uniform(1, 3)
            percentage = (weight / 100) + 1
            if option == "inflate":
                self.stockpile[item]["price"] = round(
                    self.stockpile[item]["price"] * percentage
                )
            else:
                self.stockpile[item]["price"] = round(
                    self.stockpile[item]["price"] / percentage
                )

    def random_supply(self):
        """Simulates change or variability in market supply"""
        for item in self.stockpile:
            self.stockpile[item]["quantity"] = random.randint(0, 20)
