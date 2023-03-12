from states.state import State
from decorators import *

# TODO decorator: header
# TODO decorator: input validation


class PriceChange(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("Price Change Menu")
        print("[1] Change Item Price\n[0] Go Back")
        choice = self.game.get_input()
        if choice == "1":
            self.change_price()
        elif choice == "0":
            self.exit_state()

    def render(self):
        pass

    def change_price(self):
        # TODO decorator to print header
        """
        Accepts an input item name from the user and searches
        the player's stockpile[dictionary/json] for that item.

        """
        print(">>> Changing Price <<<")
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
        new_price = input(">>> \u20B1 ")
        return new_price
