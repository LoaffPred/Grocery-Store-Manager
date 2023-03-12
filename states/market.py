from states.state import State
from util import *
import random
from decorators import *


class Market(State):
    def __init__(self, game):
        super().__init__(game)
        self.stockpile = read_json("baseStockpile.json")
        self.inflation()
        self.random_supply()

    def update(self):
        self.render()
        print("[1] Buy From Market\n[0] Go Back")
        choice = self.game.get_input()
        if choice == "1":
            self.sell()
        elif choice == "0":
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
        choice = input(">>> ")
        if choice in self.stockpile.keys():
            print("Enter quantity of {} to buy:".format(choice))
            try:
                num = int(input(">>> "))
            except:
                print("Numbers only [0-9]...")
                print("Going back to previous menu...")
            else:
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

    def inflation(self):
        items = random.sample(list(self.stockpile.keys()), k=random.randint(3, 7))
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

    def random_supply(self):
        for item in self.stockpile:
            self.stockpile[item]["quantity"] = random.randint(0, 20)
