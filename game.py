from states.main_menu import MainMenu
from os import path, getcwd
from util import *
from player import Player
from beautifultable import BeautifulTable
from pyfiglet import Figlet
from decorators import *


# TODO implement "Press [enter] to proceed..."


class Game:
    def __init__(self):
        self.running = True
        self.playing = True
        self.interface = self.setup_interface()
        self.state_stack = []
        self.load_states()
        self.player = Player()

    def game_loop(self):
        while self.playing:
            self.update()

    def update(self):
        self.state_stack[-1].update()

    def print_interface(self):
        print(self.interface)

    def load_states(self):
        self.main_menu = MainMenu(self)
        self.state_stack.append(self.main_menu)

    def setup_interface(self):
        table = BeautifulTable()
        table.set_style(BeautifulTable.STYLE_BOX)
        table.rows.append(["SCREEN"])
        table.rows.append(["OPTIONS"])

        return table

    def update_interface(self, subtable, **kwargs):
        self.interface.rows[0][0] = subtable
        if kwargs:
            subsubtable = BeautifulTable()
            subsubtable = self.format_table(subsubtable)
            subsubtable.columns.header = ["ACTIONS"]
            subsubtable.rows.append([kwargs["options"]])
            subsubtable.columns.header.alignment = BeautifulTable.ALIGN_CENTER
            subsubtable.columns.alignment = BeautifulTable.ALIGN_LEFT
            self.interface.rows[1][0] = subsubtable

    def format_table(self, table):
        table.set_style(BeautifulTable.STYLE_BOX)
        table.border.left = ""
        table.border.right = ""
        table.border.top = ""
        table.border.bottom = ""
        table.rows.separator = ""
        return table

    @input_validator("1", "2", "3", "4", "5", "6", "0", "cancel")
    def get_input(self):
        return input(">>> ")


########################################
def setup():
    base_stockpile = {
        "Orange": {"quantity": 10, "price": 57.50},
        "Apple": {"quantity": 10, "price": 44},
        "Banana": {"quantity": 10, "price": 175},
        "Grape": {"quantity": 10, "price": 395},
        "Mango": {"quantity": 10, "price": 79.50},
        "Cabbage": {"quantity": 10, "price": 148},
        "Carrot": {"quantity": 10, "price": 95},
        "Eggplant": {"quantity": 10, "price": 109},
        "Broccoli": {"quantity": 10, "price": 145},
        "Sayote": {"quantity": 10, "price": 49},
    }
    savefiles = {}

    def check_existence(filename, data):
        if not path.exists(path.join(getcwd(), filename)):
            print("[{}] file not found. Creating new file.".format(filename))
            write_json(path.join(getcwd(), filename), data)

    check_existence("baseStockpile.json", base_stockpile)
    check_existence("savefiles.json", savefiles)


if __name__ == "__main__":
    standard = Figlet()
    print(standard.renderText("Grocery Manager Simulator"))
    input("Press [enter] to proceed...")
    setup()
    game = Game()
    while game.running:
        game.game_loop()
