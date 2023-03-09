from states.state import State
from states.game_world import GameWorld


class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("This is the title screen.")
        print("[1] Play Game\n[3] Options\n[0] Exit")
        a = input(">>> ")
        if a == "1":
            if self.game.has_saved_game:
                self.check_saved_game()
            else:
                new_state = GameWorld(self.game, True)
                new_state.enter_state()
        elif a == "2":
            pass  # TODO
        elif a == "0":
            self.game.playing = False
            self.game.running = False
        else:
            print("Invalid input...")

    def render(self):
        pass

    def check_saved_game(self):
        print("Saved game detected. Would you like to start a new game?")
        print(
            "[1] Override and Start New Game\n[2] Resume Game\n[0] Cancel and Go Back"
        )
        a = input(">>> ")
        if a == "1":
            new_state = GameWorld(self.game, True)
            new_state.enter_state()
        elif a == "2":
            new_state = GameWorld(self.game, False)
            new_state.enter_state()
        elif a == "0":
            return
        else:
            print("Invalid input...")
