from states.state import State
from util import *
import random


class Market(State):
    def __init__(self, game):
        super().__init__(game)
        self.stockpile = read_json("baseStockpile.json")
        self.inflation()

    def update(self):
        self.render()
        print("[1] Buy From Market\n[0] Go Back")
        a = input(">>> ")
        if a == "1":
            self.sell()
        elif a == "0":
            self.game.player.days_played += 1
            self.exit_state()
        else:
            print("Invalid input...")

    def render(self):
        print("Welcome to the Market!")
        table = self.add_market_table()
        print(table)

    def add_market_table(self):
        basetable = self.game.get_basetable()
        market_table = self.game.to_table(self.stockpile)
        playertable = self.game.to_table(self.game.player.stockpile)

        basetable.rows[0][0] = playertable
        basetable.rows[0][1] = market_table

        return basetable

    def sell(self):
        print("Enter produce name to buy: [Case-sensitive]")
        a = input(">>> ")
        if a in self.stockpile.keys():
            print("Enter quantity of {} to buy:".format(a))
            try:
                b = int(input(">>> "))
            except:
                print("Numbers only [0-9]...")
                print("Going back to previous menu...")
            else:
                total_amount = b * self.stockpile[a]["price"]
                if b > self.stockpile[a]["quantity"]:
                    print("Buy less than or equal to what the market has...".format(a))
                elif self.game.player.balance < total_amount:
                    print("You don't have enough money to buy that...")
                else:
                    self.game.player.stockpile[a]["quantity"] += b
                    self.stockpile[a]["quantity"] -= b
                    self.game.player.balance -= total_amount
                    print("Purchase successful.")

    def inflation(self):
        # randomly choose an item to inflate
        # randomly choose whether to inflate or deflate
        # randomly choose by how much 1%, 2%, or 3%
        items = random.sample(list(self.stockpile.keys()), k=random.randint(3, 5))
        for item in items:
            option = random.choice(["inflate", "deflate"])
            chance = random.uniform(1, 3)
            percentage = (chance / 100) + 1
            if option == "inflate":
                self.stockpile[item]["price"] = round(
                    self.stockpile[item]["price"] * percentage
                )
            else:
                self.stockpile[item]["price"] = round(
                    self.stockpile[item]["price"] / percentage
                )
