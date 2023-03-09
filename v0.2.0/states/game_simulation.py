from states.state import State
from player import Player


class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(self.game)

    def update(self):
        print("Welcome to the game world!")
        print("[1] Simulate\n[2] Restock\n[0] Save and Exit")
        a = input(">>> ")
        if a == "1":
            print(">>> Simulate <<<")
        elif a == "2":
            pass  # TODO
        elif a == "3":
            self.exit_state()
        else:
            print("Invalid input...")

    def render(self):
        pass
