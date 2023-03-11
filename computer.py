from util import *
import random


class Computer:
    def __init__(self, game):
        self.game = game
        self.stockpile = read_json("baseStockpile.json")

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
                    1, self.game.player.stockpile[item]["quantity"]
                )
                self.game.player.stockpile[item]["quantity"] -= quantity
                total_item_price = quantity * self.game.player.stockpile[item]["price"]
                total_amount += total_item_price

                summary = "Customers bought {} {}, worth \u20B1 {}".format(
                    quantity, item, total_item_price
                )
                print(summary)
            except ValueError:
                continue

        self.game.player.balance += total_amount
