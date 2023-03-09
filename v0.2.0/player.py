from util import *
from prettytable import PrettyTable


class Player:
    """Represents the player, their functions, and attributes"""

    def __init__(self, is_new):
        player_data = read_json("v0.2.0\\playerData.json")
        self.name = player_data["Name"]
        self.balance = player_data["Balance"]
        self.stockpile = self.get_stockpile(is_new)

    def get_stockpile(self, is_new):
        if is_new:
            return read_json("v0.2.0\\baseStockpile.json")
        else:
            return read_json("v0.2.0\\playerStockpile.json")

    def stockpile_to_table(self):
        table = PrettyTable()
        table.field_names = ["Item", "Quantity", "Price"]
        for k, v in self.stockpile.items():
            table.add_row([k, v["quantity"], "\u20B1" + str(v["price"])])

        table.align["Item"] = "l"
        table.align["Quantity"] = "c"
        table.align["Price"] = "l"

        print(table)

    def change_price(self):
        """
        Accepts an input item name from the user and searches
        the stockpile[dictionary/json] for that item.

        """
        # TODO decorator to print header
        print(">>> Changing Price <<<")
        print("Enter item name [case-sensitive]:")
        item = input(">>> ")
        if item in self.stockpile:
            while True:
                try:
                    text = (
                        "Enter new price for [{}]. Current price is \u20B1 {}".format(
                            item, self.stockpile[item]["price"]
                        )
                    )
                    print(text)

                    new_price = float(input(">>> \u20B1 "))
                    self.stockpile[item]["price"] = new_price
                    print("Change price successful...")
                    return

                except ValueError:
                    print("Invalid input. Numbers only [0-9]...")

        else:
            print(
                "That item does not exist in your stockpile, returning to previous menu..."
            )

    def save_player_data(self):
        # TODO Loop over every data in playerData.json, then write over with actual player data
        pass
