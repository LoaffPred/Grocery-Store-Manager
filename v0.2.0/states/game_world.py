from states.state import State
from player import Player
import random


class GameWorld(State):
    def __init__(self, game, is_new):
        super().__init__(game)
        self.player = Player(is_new)

    def update(self):
        print("Welcome to the game world!")
        print("[1] Simulate\n[2] Restock\n[3] Change Prices\n[0] Save and Exit")
        a = input(">>> ")
        # Simulate
        if a == "1":
            print(">>> Simulate <<<")
            self.simulate()
        # Restock
        elif a == "2":
            pass  # TODO
        # Change Prices
        elif a == "3":
            pass
        # Exit
        elif a == "0":
            self.exit_state()

        else:
            print("Invalid input...")

    def render(self):
        pass

    def simulate(self):
        pass

    def simulate(self):
        # TODO customer buys depending on the price, have a comparison with SRP, lower the better
        # TODO format summary in table
        # TODO clean up
        """
        Simulates a customer choosing what to buy via random selection.
        Randomly selects categories, items from those categories,
        and how many of those items [if 0, then no transaction].
        Calculates and returns the weighted total of all the items bought.

            Returns:
                    total_amount (int): amount to be added to player's balance

        """
        total_amount = 0
        print(">>> Simulation summary for the week <<<")

        categories = random.sample(
            list(self.player.stockpile.keys()),
            k=random.randint(0, len(self.player.stockpile.keys())),
        )
        if categories:
            for category in categories:
                items = random.sample(
                    list(self.player.stockpile[category].keys()),
                    k=random.randint(0, len(self.player.stockpile[category].keys())),
                )

                if items:
                    for item in items:
                        quantity = random.randint(
                            1, self.player.stockpile[category][item]["quantity"]
                        )
                        self.player.stockpile[category][item]["quantity"] -= quantity
                        total_item_price = (
                            quantity * self.player.stockpile[category][item]["price"]
                        )
                        total_amount += total_item_price

                        summary = "Sold {} {}, worth \u20B1 {}".format(
                            quantity, item, total_item_price
                        )
                        print(summary)

        self.player.balance += total_amount
        print("Simulation done...")
