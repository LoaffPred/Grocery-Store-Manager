from states.main_menu import MainMenu
import json  # loaf game properties
from prettytable import PrettyTable
from os import path
from util import *
from player import Player


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
        self.has_saved_game = False  # change to None/code for multiple saved games
        self.player = Player(not self.has_saved_game)

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

    def print_table(self, stockpile):
        table = PrettyTable()
        table.field_names = ["Item", "Quantity", "Price"]
        for k, v in stockpile.items():
            table.add_row([k, v["quantity"], "\u20B1" + str(v["price"])])

        table.align["Item"] = "l"
        table.align["Quantity"] = "c"
        table.align["Price"] = "l"

        print(table)

    # def get_old_data(self, filename):
    #     return read_json(filename)

    # def create_new_data(self, filename, data):
    #     write_json(filename, data)


if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()
