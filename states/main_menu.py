from states.state import State
from states.game_world import GameWorld


class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("This is the title screen.")
        print("[1] Play Game\n[2] Options\n[0] Exit")
        a = input(">>> ")
        # Play Game
        if a == "1":
            if self.game.has_saved_game:
                self.override_game()
            else:
                self.new_game()
        # Options [optional]
        elif a == "2":
            pass  # TODO
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

    def override_game(self):
        print("Saved game detected.")
        print(
            "[1] Resume Game\n[2] Override and Start New Game\n[0] Cancel and Go Back"
        )
        a = input(">>> ")
        # Resume
        if a == "1":
            print("Welcome back {}!".format(self.game.player.name))
            new_state = GameWorld(self.game)
            new_state.enter_state()
        # Override
        elif a == "2":
            self.new_game()
        # Cancel and Go Back
        elif a == "0":
            return
        else:
            print("Invalid input...")

    def new_game(self):
        self.game.player.name = self.get_username()
        new_state = GameWorld(self.game)
        new_state.enter_state()
