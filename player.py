from owners import Owner


class Player(Owner):
    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.level = 0
        self.gamestate = "MainMenu"

    def change_price(self):
        # decorator to print header
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
