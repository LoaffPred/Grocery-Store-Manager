from states.state import State
from states.game_simulation import GameWorld


class Title(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        print("This is the title screen.")
        print("[1] New Game\n[2] Resume Game\n[3] Options\n[0] Exit")
        a = input(">>> ")
        if a == "1":
            new_state = GameWorld(self.game)
            new_state.enter_state()
        elif a == "2":
            pass # TODO
        elif a == "3":
            pass # TODO
        elif a == "0":
            self.game.playing = False
            self.game.running = False
        else:
            print("Invalid input...")
        

    def render(self):
        pass