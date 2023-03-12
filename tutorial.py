"""Separate files for tutorial message"""


def transition_pause(func):
    def inner():
        func()
        input("Press [enter] to proceed...")

    return inner


def print_header(header):
    def outer(func):
        def inner():
            print("====================>>> ", end="")
            for l in header:
                print(l + " ", end="")
            print("<<<====================")
            func()

        return inner

    return outer


@transition_pause
@print_header("HOW TO PLAY")
def print_tutorial():
    print(
        """
Hello player, Welcome to Grocery Manager Simulator!

In this game, you will be managing a gorcery store with a set amount of produce.
At the end of the month (28 days), you will have to pay your monthly bills.
You lose if you do not have enough money to pay your bills, also, the monthly bills increase each month.

[1] Simulate - simulate a day of customers purchasing produce from your grocery.

[2] Restock - brings you to the market where you can buy more produce.
The market prices and quantities may vary per day, and every visit to the market is considered a day.

[3] Change Prices - allows you to change the prices of your produce.

[0] Save and Exit - save your progress and go back to the main menu.

Good luck and Have Fun!
"""
    )
