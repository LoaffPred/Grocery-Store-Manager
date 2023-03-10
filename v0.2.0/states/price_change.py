from states.state import State

# TODO decorator: header
# TODO decorator: input validation


class PriceChange(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("Price Change Menu")
        self.game.print_table(self.game.player.stockpile)
        print("[1] Change Item Price\n[0] Go Back")
        a = input(">>> ")
        if a == "1":
            self.change_price()
        elif a == "0":
            self.exit_state()
        else:
            print("Invalid input...")

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
                try:
                    text = (
                        "Enter new price for [{}]. Current price is \u20B1 {}".format(
                            item, self.game.player.stockpile[item]["price"]
                        )
                    )
                    print(text)

                    new_price = float(input(">>> \u20B1 "))
                    self.game.player.stockpile[item]["price"] = new_price
                    print("Change price successful...")
                    return

                except ValueError:
                    print("Invalid input. Numbers only [0-9]...")

        else:
            print(
                "That item does not exist in your stockpile, returning to previous menu..."
            )
