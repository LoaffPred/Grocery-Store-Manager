from owner import Owner
from utilities import *


class Player(Owner):
    """Represents the player, their functions, and attributes"""

    def __init__(self):
        super().__init__()  # stockpile
        self.name = ""
        self.balance = read_json("playerData.json")["Balance"]
        self.level = 0

    def change_price(self):
        """
        Accepts an input item name from the user and searches
        the stockpile[dictionary/json] for that item.

        """
        # TODO decorator to print header
        print(">>> Changing Price <<<")
        print("Enter item name [case-sensitive]:")
        item_input = input(">>> ")
        for category, item_dict in self.stockpile.items():
            for item in item_dict.keys():
                if item_input == item:
                    while True:
                        try:
                            text = "Enter new price for [{}]. Current price is \u20B1 {}".format(
                                item, self.stockpile[category][item]["price"]
                            )
                            print(text)

                            new_price = float(input(">>> \u20B1 "))
                            self.stockpile[category][item]["price"] = new_price
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
