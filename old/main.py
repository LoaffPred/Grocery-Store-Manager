import display
from player import Player
from Testing.prettytable_test import to_table  # change
from computer import Computer
from util import *


# TODO implement "Press [enter] to proceed..."
# TODO decorator idea: yes/no confirmation for prompts/questions i.e., Are you sure? [y/n]
# TODO decorator idea: input validator, parameters(*inputs, type?)


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

    player.save_player_data()
    write_json("gameProperties.json", game)


def check_saved_game():
    if game["HasSavedGame"]:
        print(
            "Saved game detected, do you want to overwrite and start a new game? [y/n]"
        )
        a = input(">>> ").lower()
        if a == "y":
            game["GameState"] = "Running"
            game["HasSavedGame"] = True
        elif a == "n":
            game["GameState"] = "MainMenu"
        else:
            print("Invalid Input...")
    else:
        print("No saved game...")


def mainmenu(choice):
    if choice == "1":  # NEW GAME
        if check_saved_game():
            print(">>> New Game <<<")
            player.name = get_username()
            player.set_new_stockpile("baseStockpile.json", "playerStockpile.json")
            computer.set_new_stockpile("baseStockpile.json", "computerStockpile.json")
            game["GameState"] = "Running"

            print(display.greetings.format(player.name))
    elif choice == "2":
        print("Continue")
        player.get_stockpile("playerStockpile.json")
        computer.get_stockpile("computerStockpile.json")
        game["GameState"] = "Running"
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
        game["GameState"] = "MainMenu"
    else:
        print("Not a recognized action.")


def main():
    while True:  # Game loop
        while game["GameState"] == "MainMenu":
            print(display.main_menu)
            choice = input(">>> ")
            mainmenu(choice)

        while game["GameState"] == "Running":
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
    game = read_json("gameProperties.json")
    main()
