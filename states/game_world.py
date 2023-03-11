from states.state import State
from states.price_change import PriceChange
from states.market import Market
from states.monthlydues import MonthlyDue
import random


class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("Welcome to the game world!")
        self.render()
        print("[1] Simulate\n[2] Restock\n[3] Change Prices\n[0] Save and Exit")
        a = input(">>> ")
        # Simulate
        if a == "1":
            print(">>> Simulate <<<")
            self.simulate()
            self.game.player.days_played += 1
            if self.game.player.days_played % 28 == 0:
                new_state = MonthlyDue(self.game)
                new_state.enter_state()
        # Restock
        elif a == "2":
            new_state = Market(self.game)
            new_state.enter_state()
        # Change Prices
        elif a == "3":
            new_state = PriceChange(self.game)
            new_state.enter_state()
        # Save and Exit
        elif a == "0":
            self.save_game()
            self.exit_state()

        else:
            print("Invalid input...")

    def render(self):
        print("Day", self.game.player.days_played)
        table = self.add_playertable()
        new_table = table.columns[:1]
        print(new_table)
        print("Your balance: \u20B1", self.game.player.balance)

    def simulate(self):
        self.buy()

    def save_game(self):
        self.game.has_saved_game = True
        self.game.player.save_player_data()
        self.game.save_game_data()

    def add_playertable(self):
        basetable = self.game.get_basetable()
        table = self.game.to_table(self.game.player.stockpile)

        basetable.rows[0][0] = table

        return basetable

    def buy(self):
        # TODO customer buys depending on the price, have a comparison with SRP, lower the better
        # TODO format summary in table
        # TODO clean up
        """
        Simulates a customer choosing what to buy via random selection.
        Randomly selects categories, items from those categories,
        and how many of those items [if 0, then no transaction].
        Calculates and returns the weighted total of all the items bought.
        """
        total_amount = 0
        print(">>> Simulation summary for the week <<<")

        items = random.sample(
            list(self.game.player.stockpile.keys()),
            k=random.randint(0, len(self.game.player.stockpile.keys())),
        )

        for item in items:
            try:
                quantity = random.randint(
                    1, 5 % (self.game.player.stockpile[item]["quantity"] + 1)
                )
                self.game.player.stockpile[item]["quantity"] -= quantity
                total_item_price = quantity * self.game.player.stockpile[item]["price"]
                total_amount += total_item_price

                summary = "Customers bought {} {}, worth \u20B1 {}".format(
                    quantity, item, total_item_price
                )
                print(summary)
            except ValueError or ZeroDivisionError:
                continue

        self.game.player.balance += total_amount
