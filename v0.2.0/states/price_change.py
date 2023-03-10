from states.state import State


class PriceChange(State):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player

    def update(self):
        print("Price Change Menu")
        self.player.print_table
        print("[1] Change Item Price\n[0] Go Back")
        a = input(">>> ")
        if a == "1":
            self.change_price()
        elif a == "0":
            self.exit_state()
        else:
            print("Invalid input...")


    def change_price(self):
        """
        Accepts an input item name from the user and searches
        the player's stockpile[dictionary/json] for that item.

        """
        # TODO decorator to print header
        print(">>> Changing Price <<<")
        print("Enter item name [case-sensitive]:")
        item = input(">>> ")
        if item in self.player.stockpile:
            while True:
                try:
                    text = (
                        "Enter new price for [{}]. Current price is \u20B1 {}".format(
                            item, self.player.stockpile[item]["price"]
                        )
                    )
                    print(text)

                    new_price = float(input(">>> \u20B1 "))
                    self.player.stockpile[item]["price"] = new_price
                    print("Change price successful...")
                    return

                except ValueError:
                    print("Invalid input. Numbers only [0-9]...")

        else:
            print(
                "That item does not exist in your stockpile, returning to previous menu..."
            )
