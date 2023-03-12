test = [
    "-100",
    "10.0",
    "-10.0",
]

for x in test:
    print("Digit", x.isdigit())
    print("Decimal", x.isdecimal())
    print("Numeric", x.isnumeric())
    print("Alphanumeric", x.isalnum())

try:
    print(float("10.0"))
    print(float("-10"))
    print(float("-10.0"))
except:
    print("Cant do that")
