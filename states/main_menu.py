from states.state import State
from states.game_world import GameWorld
from util import *
from decorators import *
from beautifultable import BeautifulTable
import tutorial


class MainMenu(State):
    """Main Menu class - handles all events and properties of the main menu.
    Allows starting of a new game, loading and resuming a saved game, and deleting a saved game
    """

    def __init__(self, game):
        super().__init__(game)
        self.actions = (
            "[1] New Game\n[2] Load Save\n[3] Delete Save\n[4] How To Play\n[0] Exit"
        )

    @print_header("MAIN MENU")
    def update(self):
        """Runs and updates logic and events of the Main Menu"""
        self.game.update_interface(self.create_menutable(), options=self.actions)
        self.game.print_interface()
        choice = self.game.get_input()
        # ======================== Play Game ======================== #
        if choice == "1":
            username = self.get_username()
            if username == "cancel":
                return
            if username == None:
                return
            new_state = GameWorld(self.game, username, self.new_game_setup())
            new_state.enter_state()
        # ======================== Load Save ======================== #
        elif choice == "2":
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
        # ======================== Delete Save File ======================== #
        elif choice == "3":
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
            except Exception as e:
                print(e, "That save file does not exist...")
        # ======================== Delete Save File ======================== #
        elif choice == "4":
            tutorial.print_tutorial()
        # ======================== Exit ======================== #
        elif choice == "0":
            self.game.playing = False
            self.game.running = False

    def create_menutable(self):
        """Creates table for Main Menu interface"""
        table = BeautifulTable()
        table.rows.append(["MAIN MENU"])
        table = self.game.format_table(table)
        return table

    @alpha_only
    def get_username(self):
        """Used as target function for decorator"""
        print("Enter your name, enter [cancel] to go back:")
        name = input(">>> ")
        return name

    def new_game_setup(self):
        """Provides default data for new games"""
        balance = 10000
        days_played = 0
        stockpile = read_json("baseStockpile.json")
        data = {"Balance": balance, "DaysPlayed": days_played, "Stockpile": stockpile}
        return data
