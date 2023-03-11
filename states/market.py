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
        player_table = self.game.get_table(self.game.player.stockpile).get_string(
            fields=["Item", "Quantity"]
        )
        market_table = self.game.get_table(self.stockpile).get_string()

        interface = "{}\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}".format(
            player_table, market_table
        )
        print(interface)

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
