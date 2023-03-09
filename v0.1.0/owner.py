from utilities import *


class Owner:
    def __init__(self):
        self.stockpile = {}

    # decorator idea: verify if stockpile is dictionary,
    # if filename ends with .json
    def set_new_stockpile(self, filename_source, filename_own):
        self.stockpile = read_json(filename_source)
        write_json(filename_own, self.stockpile)

    def get_stockpile(self, filename):
        self.stockpile = read_json(filename)

    def save_stockpile(self, filename):
        write_json(filename, self.stockpile)
