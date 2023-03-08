from prettytable import PrettyTable
import pickle

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
    table.add_column(
        "Quantity",
    )

table.align = "l"
print(table)

# if __name__ == "__main__":

with open("data.pickle", "wb") as file:
    pickle.dump(stockpile, file)
