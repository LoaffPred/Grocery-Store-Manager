from states.state import State
from player import Player
import random
from states.price_change import PriceChange
from states.market import Market


class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("Welcome to the game world!")
        print("[1] Simulate\n[2] Restock\n[3] Change Prices\n[0] Save and Exit")
        a = input(">>> ")
        # Simulate
        if a == "1":
            print(">>> Simulate <<<")
            self.simulate()
        # Restock
        elif a == "2":
            new_state = Market(self.game)
            new_state.enter_state()
        # Change Prices
        elif a == "3":
            new_state = PriceChange(self.game)
            new_state.enter_state()
        # Save and Exit
        elif a == "0":
            self.save_game()
            self.exit_state()

        else:
            print("Invalid input...")

    def render(self):
        print(self.game.get_table(self.game.player.stockpile))

    def simulate(self):
        self.game.computer.buy()

    def save_game(self):
        self.game.has_saved_game = True
        self.game.player.save_player_data()
        self.game.save_game_data()
