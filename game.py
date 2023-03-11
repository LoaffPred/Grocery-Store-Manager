from states.main_menu import MainMenu
import json  # load game properties
from os import path, getcwd
from util import *
from player import Player
from computer import Computer
from beautifultable import BeautifulTable


# TODO implement "Press [enter] to proceed..."
# TODO decorator idea: yes/no confirmation for prompts/questions i.e., Are you sure? [y/n]
# TODO decorator idea: input validator, parameters(*inputs, type?)


class Game:
    def __init__(self):
        # game settings
        self.running = True
        self.playing = True
        self.state_stack = []
        self.load_states()
        self.has_saved_game = read_json("gameData.json")[
            "HasSavedGame"
        ]  # change to None/code for multiple saved games
        self.player = Player(not self.has_saved_game)
        self.computer = Computer(self)

    def game_loop(self):
        while self.playing:
            self.update()
            self.render()

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        self.state_stack[-1].render()

    def load_states(self):
        self.main_menu = MainMenu(self)
        self.state_stack.append(self.main_menu)

    def get_basetable(self):
        table = BeautifulTable()
        table.rows.append(["Heading 1", "Heading 2"])
        table.rows.append(["Subtable 1", "Subtable 2"])

        return table

    def save_game_data(self):
        data = {"HasSavedGame": self.has_saved_game}
        write_json("gameData.json", data)


def setup():
    if not path.exists(path.join(getcwd(), "baseStockpile.json")):
        print("[baseStockpile.json] file not found. Can't start game.")
        raise SystemExit()

    if not path.exists(path.join(getcwd(), "gameData.json")):
        data = {"HasSavedGame": False}
        write_json(path.join(getcwd(), "gameData.json"), data)


if __name__ == "__main__":
    setup()
    game = Game()
    while game.running:
        game.game_loop()
