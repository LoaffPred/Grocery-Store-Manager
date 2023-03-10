from util import *


class Player:
    """Represents the player, their functions, and attributes"""

    def __init__(self, is_new):
        player_data = self.get_player_data(is_new)
        self.name = player_data["Name"]
        self.balance = player_data["Balance"]
        # decorator idea: verify if stockpile is dictionary,
        # if filename ends with .json
        self.stockpile = self.get_stockpile(is_new)

    def get_player_data(self, is_new):
        if is_new:
            data = {"Name": "", "Balance": 1000}
            return get_data("v0.2.0\\playerData.json", data)
        else:
            return read_json("v0.2.0\\playerData.json")

    def get_stockpile(self, is_new):
        if is_new:
            return get_data("v0.2.0\\playerStockpile.json", read_json("v0.2.0\\baseStockpile.json"))
        else:
            return read_json("v0.2.0\\playerStockpile.json")

    def save_player_data(self):
        data = {"Name": self.name, "Balance": self.balance}
        write_json("v0.2.0\\playerStockpile.json", data)
