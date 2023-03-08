import display
from player import Player
from Testing.prettytable_test import to_table
from computer import Computer


def alpha_only(func):
    def wrapper():
        while True:
            temp = func()
            if temp.isalpha():
                return temp
            else:
                print("Only alphabetical [a-zA-Z] letters are allowed.")

    return wrapper


@alpha_only
def get_username():
    player_name = input("Enter your name: ")
    return player_name


def save_game():
    player.save_stockpile("playerStockpile.json")
    computer.save_stockpile("computerStockpile.json")


def mainmenu(choice):
    if choice == "1":
        print("New Game")
        player.get_new_stockpile("playerStockpile.json")
        computer.get_new_stockpile("computerStockpile.json")
        player.gamestate = "Running"
    elif choice == "2":
        print("Continue")
        player.get_stockpile("playerStockpile.json")
        computer.get_stockpile("computerStockpile.json")
        player.gamestate = "Running"
    elif choice == "3":
        print("Options")
    elif choice == "0":
        print(display.quit_game)
        raise SystemExit
    else:
        print("Not a recognized action.")


def actions(choice):
    if choice == "1":
        print("Simulate")
        total_amount = computer.buy(player.stockpile)
        player.balance += total_amount
        print("Earned = \u20B1", total_amount)
        print("Balance = \u20B1", player.balance)
    elif choice == "2":
        print("Restock")
    elif choice == "3":
        print("Change price")
        player.change_price()
    elif choice == "0":
        print("Saving game, do not close...")
        save_game()
        print("Game succesfully saved...")
        player.gamestate = "MainMenu"
    else:
        print("Not a recognized action.")


def main():
    player.name = get_username()
    print(display.greetings.format(player.name))

    while True:  # Game loop
        while player.gamestate == "MainMenu":
            print(display.main_menu)
            choice = input(">>> ")
            mainmenu(choice)

        while player.gamestate == "Running":
            # format stockpile to table then print
            table = to_table(player.stockpile)
            print(display.stockpile_header)
            print(table)

            print(display.actions)
            choice = input(">>> ")
            actions(choice)


if __name__ == "__main__":
    player = Player()
    computer = Computer()
    main()
