import json
from prettytable import PrettyTable

table = PrettyTable()

# with open("TESTING\\stockpile.json", "r") as file:
#     data = json.load(file)

stockpile = {
    "Fruits": {
        "Orange": {"quantity": 0, "price": 0},
        "Apple": {"quantity": 0, "price": 0},
        "Banana": {"quantity": 0, "price": 0},
        "Grape": {"quantity": 0, "price": 0},
        "Mango": {"quantity": 0, "price": 0},
    },
    "Vegetables": {
        "Cabbage": {"quantity": 0, "price": 0},
        "Carrot": {"quantity": 0, "price": 0},
        "Eggplant": {"quantity": 0, "price": 0},
        "Squash": {"quantity": 0, "price": 0},
        "Chayote": {"quantity": 0, "price": 0},
    },
}

stockpile = str(stockpile)
data = json.loads(stockpile)
