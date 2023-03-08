import json


class Player:
    def __init__(self):
        # self.name = ""
        self.balance = 1000
        self.level = 0
        self.gamestate = "MainMenu"
        self.newgame = True
        self.stockpile = {}

    def new_stockpile(self):
        with open("stockpile.json", "r") as file:
            self.stockpile = json.load(file)
