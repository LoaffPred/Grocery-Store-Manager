from states.state import State
from states.gameover import GameOver


class MonthlyDue(State):
    def __init__(self, game):
        super().__init__(game)
        self.bill = 10000

    def update(self):
        self.increase_bill()
        self.render()
        if self.game.player.balance < self.bill:
            new_state = GameOver(self.game)
            new_state.enter_state()
            pass
        else:
            self.game.player.balance -= self.bill
            print("Monthly bills paid.")

            self.exit_state()

    def render(self):
        print("A month has passed. It's time to pay...")
        print("Monthly Dues: \u20B1 " + str(self.bill))
        print("Your Balance: \u20B1 " + str(self.game.player.balance))

    def increase_bill(self):
        # starts increasing on the second month
        if self.game.player.days_played > 28:
            percentage = ((self.game.player.days_played // 28) / 10) + 1
            self.bill *= percentage
