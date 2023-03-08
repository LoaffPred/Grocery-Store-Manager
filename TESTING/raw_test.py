import random
from prettytable import PrettyTable
import json


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

table = PrettyTable()

for section, item_dict in stockpile.items():
    table.add_column(section, list(item_dict.keys()))
    table.add_column("Quantity", list(item_dict.values()))

table.align = "l"
print(table)




print(buy(stockpile))
print(buy(stockpile))
print(buy(stockpile))
print(buy(stockpile))

