from states.state import State


class GameOver(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        self.render()
        while len(self.game.state_stack) > 1:
            self.game.state_stack.pop()

    def render(self):
        print("You were not able to pay off your monthly bills.")
        print("The government has seized your business.")
        print("You have no future now")
        print(">>> GAME OVER <<<")
