import random
from owner import Owner


class Computer(Owner):
    def __init__(self):
        super().__init__()

    def buy(self, stockpile):
        # TODO customer buys depending on the price, have a comparison with SRP, lower the better
        # TODO format summary in table
        """
        Simulates a customer choosing what to buy via random selection.
        Randomly selects categories, items from those categories,
        and how many of those items [if 0, then no transaction].
        Calculates and returns the weighted total of all the items bought.

            Parameters:
                    stockpile (dictionary): containins stockpile items, their
                                        quantity, and price

            Returns:
                    total_amount (int): amount to be added to player's balance

        """
        total_amount = 0
        print(">>> Simulation summary for the week <<<")

        categories = random.sample(
            list(stockpile.keys()), k=random.randint(0, len(stockpile.keys()))
        )
        if categories:
            for category in categories:
                items = random.sample(
                    list(stockpile[category].keys()),
                    k=random.randint(0, len(stockpile[category].keys())),
                )

                if items:
                    for item in items:
                        quantity = random.randint(
                            0, stockpile[category][item]["quantity"]
                        )
                        stockpile[category][item]["quantity"] -= quantity
                        total_item_price = quantity * stockpile[category][item]["price"]
                        total_amount += total_item_price

                        summary = "Sold {} {}, worth \u20B1 {}".format(
                            quantity, item, total_item_price
                        )
                        print(summary)

        return total_amount
