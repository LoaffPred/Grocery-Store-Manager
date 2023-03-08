from prettytable import PrettyTable

# stockpile = {
#     "Fruits": {
#         "Orange": {"quantity": 0, "price": 0},
#         "Apple": {"quantity": 0, "price": 0},
#         "Banana": {"quantity": 0, "price": 0},
#         "Grape": {"quantity": 0, "price": 0},
#         "Mango": {"quantity": 0, "price": 0},
#     },
#     "Vegetables": {
#         "Cabbage": {"quantity": 0, "price": 0},
#         "Carrot": {"quantity": 0, "price": 0},
#         "Eggplant": {"quantity": 0, "price": 0},
#         "Squash": {"quantity": 0, "price": 0},
#         "Chayote": {"quantity": 0, "price": 0},
#     },
# }


def to_table(stockpile):
    table = PrettyTable()

    table.field_names = ["Item", "Quantity"]
    for category, item_dict in stockpile.items():
        for item, properties in item_dict.items():
            table.add_row([item, properties["quantity"]])

    table.align["Item"] = "l"
    table.align["Quantity"] = "c"

    return table


# table = get_table(stockpile)
