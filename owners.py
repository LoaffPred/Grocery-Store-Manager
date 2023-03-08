import json


class Owner:
    def __init__(self):
        self.stockpile = {}

    # decorator idea: verify if stockpile is dictionary,
    # if filename ends with .json
    def get_new_stockpile(self, filename):
        with open("baseStockpile.json", "r") as file:
            self.stockpile = json.load(file)

        with open(filename, "w") as file:
            json.dump(self.stockpile, file, indent=4)

    def get_stockpile(self, filename):
        with open(filename, "r") as file:
            self.stockpile = json.load(file)

    def save_stockpile(self, filename):
        with open(filename, "w") as file:
            json.dump(self.stockpile, file, indent=4)
