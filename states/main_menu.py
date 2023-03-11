from states.state import State
from states.game_world import GameWorld
from util import *


class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("This is the title screen.")
        print("[1] New Game\n[2] Load Save\n[3] Delete Save\n[0] Exit")
        a = input(">>> ")
        # Play Game
        if a == "1":
            username = self.get_username()
            new_state = GameWorld(self.game, username, self.new_game_setup())
            new_state.enter_state()
        # Load Save
        elif a == "2":
            print("Saved Games:")
            for save in read_json("savefiles.json").keys():
                print(">", save)
            print("Enter name of save to load: [Case-sensitive]")
            name = input(">>> ")
            try:
                player_data = read_json("savefiles.json")[name]
                new_state = GameWorld(self.game, name, player_data)
                new_state.enter_state()
            except:
                print("That save file does not exist...")
        elif a == "3":
            savefiles = read_json("savefiles.json")
            print("Saved Games:")
            for save in savefiles.keys():
                print(">", save)
            print("Enter name of save to delete: [Case-sensitive]")
            save = input(">>> ")
            try:
                savefiles.pop(save)
                write_json("savefiles.json", savefiles)
                print("Save successfuly deleted.")
            except:
                print("That save file does not exist...")
        # Exit
        elif a == "0":
            self.game.playing = False
            self.game.running = False
        else:
            print("Invalid input...")

    def render(self):
        pass

    def get_username(self):
        # TODO decorator: input validation
        print("Enter your name:")
        a = input(">>> ")
        return a

    def new_game_setup(self):
        balance = 10000
        days_played = 0
        stockpile = read_json("baseStockpile.json")

        data = {"Balance": balance, "DaysPlayed": days_played, "Stockpile": stockpile}

        return data
