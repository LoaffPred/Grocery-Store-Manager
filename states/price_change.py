from states.state import State
from decorators import *


class PriceChange(State):
    """Price Change class - handles all events and properties of the price change event.
    Accepts only numeric input"""

    def __init__(self, game):
        super().__init__(game)

    @print_header("PRICE CHANGE MENU")
    def update(self):
        """Runs and updates logic and events of the price change event"""
        print("[1] Change Item Price\n[0] Go Back")
        choice = self.game.get_input()
        # ======================== Change Item Price ======================== #
        if choice == "1":
            self.change_price()
        # ======================== Go Back ======================== #
        elif choice == "0":
            self.exit_state()

    def change_price(self):
        """
        Accepts an input item name from the user and searches
        the player's stockpile for that item, and allows the player
        to change the price. Requires the price to be 'reasonable'
        """

        print("Enter item name [case-sensitive]:")
        item = input(">>> ")
        if item in self.game.player.stockpile:
            while True:
                text = "Enter new price for [{}]. Current price is \u20B1 {}".format(
                    item, self.game.player.stockpile[item]["price"]
                )
                print(text)
                new_price = self.get_new_price()
                if new_price:
                    self.game.player.stockpile[item]["price"] = new_price
                    print("Change price successful...")
                return
        else:
            print(
                "That item does not exist in your stockpile, returning to previous menu..."
            )

    @limit_input(0, 500)
    @num_only
    def get_new_price(self):
        """Used as a target function for decorators"""
        new_price = input(">>> \u20B1 ")
        return new_price
