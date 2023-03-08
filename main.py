import display
from player import Player
from TESTING.prettytable_test import to_table
import json
from customer import Customer


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


def mainmenu(choice):
    if choice == "1":
        print("New Game")
        player.gamestate = "Running"
    elif choice == "2":
        print("Continue")
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
        print("simulate")
        price = customer.buy(player.stockpile, 10)
        player.balance += price
        print("Earned = \u20B1", price)
        print("Balance = \u20B1", player.balance)
    elif choice == "2":
        print("restock")
    elif choice == "0":
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
            if player.newgame:
                player.new_stockpile()
                player.newgame = False
            else:
                # format stockpile to table then print
                table = to_table(player.stockpile)
                print(display.stockpile_header)
                print(table)

                print(display.actions)
                choice = input(">>> ")
                actions(choice)


if __name__ == "__main__":
    player = Player()
    customer = Customer()
    main()
