import random


class Customer:
    def set_max_reps(func):
        def wrapper(self, stockpile, reps):
            max_reps = 30
            if reps > max_reps:
                return 0
            else:
                return func(self, stockpile, reps)

        return wrapper

    @set_max_reps
    def buy(self, stockpile, reps):  # TODO check if stockpile is empty, else dont buy
        price = 0
        i = 0
        while i < reps:
            print("Customer is buying...")
            category = random.choice(list(stockpile.keys()))
            item = random.choice(list(stockpile[category].keys()))
            if stockpile[category][item]["quantity"] <= 0:
                continue
            else:
                stockpile[category][item]["quantity"] -= 1
                price += stockpile[category][item]["price"]
                i += 1

        return price
