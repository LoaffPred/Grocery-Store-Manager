from tabulate import tabulate, SEPARATING_LINE
from util import *

stockpile = {
    "Orange": {"quantity": 10, "price": 57.50},
    "Apple": {"quantity": 10, "price": 44},
    "Banana": {"quantity": 10, "price": 175},
    "Grape": {"quantity": 10, "price": 395},
}

items = list(stockpile.keys())
table = [
    [
        items[0],
        stockpile[items[0]]["quantity"],
        stockpile[items[0]]["price"],
        items[1],
        stockpile[items[1]]["quantity"],
        stockpile[items[1]]["price"],
    ],
]
header = [
    "PLAYER STOCKPILE\nITEM",
    "\nQUANTITY",
    "\nPRICE",
    "MARKET STOCKPILE\nITEM",
    "\nQUANTITY",
    "\nPRICE",
]

print(tabulate(table, header, tablefmt="grid"))
