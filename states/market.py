from states.state import State
from util import *
import random
from decorators import *
from beautifultable import BeautifulTable


class Market(State):
    def __init__(self, game_world, game, worldtable):
        super().__init__(game)
        self.game_world = game_world
        self.stockpile = read_json("baseStockpile.json")
        self.inflation()
        self.random_supply()
        self.create_markettable()
        self.game_world.worldtable.columns.append([""], header="MARKET")

    def update(self):
        self.update_markettable()
        self.game_world.update_worldtable()
        self.game.update_interface(
            self.game_world.worldtable, options="[1] Buy From Market\n[0] Go Back"
        )
        self.game.print_interface()
        choice = self.game.get_input()
        if choice == "1":
            self.sell()
        elif choice == "0":
            del self.game_world.worldtable.columns["MARKET"]
            self.game.player.days_played += 1
            self.exit_state()
        else:
            print("Invalid input...")

    def create_markettable(self):
        table = BeautifulTable()
        table.columns.header = ["Item", "Quantity", "Price"]
        for k, v in self.stockpile.items():
            table.rows.append([k, v["quantity"], "\u20B1 " + str(v["price"])])

        table = self.game.format_table(table)
        table.columns.header.alignment = BeautifulTable.ALIGN_CENTER
        table.columns.alignment["Price"] = BeautifulTable.ALIGN_LEFT

        return table

    def update_markettable(self):
        self.game_world.worldtable.columns["MARKET"] = [self.create_markettable()]

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
