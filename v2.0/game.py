from states.main_menu import Title


class Game:
    def __init__(self) -> None:
        # game settings
        self.running = True
        self.playing = True
        self.state_stack = []
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.update()
            self.render()

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        self.state_stack[-1].render()

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)


if __name__ == "__main__":
    game = Game()
    while game.running:
        game.game_loop()
