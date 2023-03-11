from states.state import State
from util import *


class Market(State):
    def __init__(self, game):
        super().__init__(game)
        self.stockpile = read_json("baseStockpile.json")

    def update(self):
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
        player_table = self.add_market_table()
        print(player_table)

    def add_market_table(self):
        # player_table = self.game.get_table???????(self.game.player.stockpile)
        column1 = [key for key in self.stockpile]
        column2 = [value["quantity"] for _, value in self.stockpile.items()]

        player_table.add_column("", ["" for _ in enumerate(self.stockpile)])
        player_table.add_column("Item", column1)
        player_table.add_column("Quantity", column2)

        player_table.add_row(["", "", "", "", "", ""])

        return player_table

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
