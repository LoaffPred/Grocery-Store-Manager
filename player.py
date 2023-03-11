from util import *


class Player:
    """Represents the player, their functions, and attributes"""

    def __init__(self):
        self.name = ""
        self.balance = 10000
        # decorator idea: verify if stockpile is dictionary,
        # if filename ends with .json
        self.stockpile = {}
        self.days_played = 0

    def load_player_data(self, data):
        self.balance = data["Balance"]
        self.days_played = data["DaysPlayed"]
        self.stockpile = data["Stockpile"]

    def save_player_data(self):
        data = {
            "Balance": self.balance,
            "DaysPlayed": self.days_played,
            "Stockpile": self.stockpile,
        }
        savefile = read_json("savefiles.json")
        savefile[self.name] = data
        write_json("savefiles.json", savefile)
