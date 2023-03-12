from states.state import State
from decorators import *


class GameOver(State):
    """Game Over class - handles all events and properties of the game over event"""

    def __init__(self, game):
        super().__init__(game)

    @print_header("GAME OVER")
    def update(self):
        """Clears the state_state and returns to main menu"""
        self.render()
        while len(self.game.state_stack) > 1:
            self.game.state_stack.pop()

    def render(self):
        print("You were not able to pay off your monthly bills.")
        print("The government has seized your business.")
        print("You have no future now")
        print(">>> GAME OVER <<<")
