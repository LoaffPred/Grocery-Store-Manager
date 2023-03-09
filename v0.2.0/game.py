from states.main_menu import MainMenu
import json

# TODO implement "Press [enter] to proceed..."
# TODO decorator idea: yes/no confirmation for prompts/questions i.e., Are you sure? [y/n]
# TODO decorator idea: input validator, parameters(*inputs, type?)


class Game:
    def __init__(self) -> None:
        # game settings
        self.running = True
        self.playing = True
        self.state_stack = []
        self.load_states()
        self.has_saved_game = False  # change to None/code for multiple saved games

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


if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()
