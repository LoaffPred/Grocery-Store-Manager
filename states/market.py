from states.state import State
from util import *


class Market(State):
    def __init__(self, game):
        super().__init__(game)
        self.stockpile = read_json("baseStockpile.json")

    def update(self):
        self.render()
        print("[1] Buy From Market\n[0] Go Back")
        a = input(">>> ")
        if a == "1":
            self.sell()
        elif a == "0":
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

        basetable[0][0] = playertable
        basetable[0][1] = market_table

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
        pass
