from states.main_menu import MainMenu
import json  # load game properties
from os import path, getcwd
from util import *
from player import Player
from beautifultable import BeautifulTable
from pyfiglet import Figlet


# TODO implement "Press [enter] to proceed..."
# TODO decorator idea: yes/no confirmation for prompts/questions i.e., Are you sure? [y/n]
# TODO decorator idea: input validator, parameters(*inputs, type?)


class Game:
    def __init__(self):
        self.running = True
        self.playing = True
        self.state_stack = []
        self.load_states()
        self.player = Player()

    def game_loop(self):
        while self.playing:
            self.update()

    def update(self):
        self.state_stack[-1].update()

    def load_states(self):
        self.main_menu = MainMenu(self)
        self.state_stack.append(self.main_menu)

    def get_basetable(self):
        table = BeautifulTable()
        table.columns.header = ["Player", "Market"]
        table.rows.append(["Player Stockpile", "Market Stockpile"])
        table.set_style(BeautifulTable.STYLE_BOX)

        return table

    def to_table(self, stockpile):
        table = BeautifulTable()
        table.columns.header = ["Item", "Quantity", "Price"]
        for k, v in stockpile.items():
            table.rows.append([k, v["quantity"], "\u20B1 " + str(v["price"])])

        table.set_style(BeautifulTable.STYLE_BOX)
        table.border.left = ""
        table.border.right = ""
        table.border.top = ""
        table.border.bottom = ""
        table.rows.separator = ""
        table.columns.alignment["Price"] = BeautifulTable.ALIGN_LEFT

        return table


def setup():
    if not path.exists(path.join(getcwd(), "baseStockpile.json")):
        print("[baseStockpile.json] file not found. Can't start game.")
        raise SystemExit()

    if not path.exists(path.join(getcwd(), "gameData.json")):
        data = {"HasSavedGame": False}
        write_json(path.join(getcwd(), "gameData.json"), data)


if __name__ == "__main__":
    standard = Figlet()
    print(standard.renderText("Grocery Manager Simulator"))
    input("Press [enter] to proceed...")
    # setup()
    game = Game()
    while game.running:
        game.game_loop()
