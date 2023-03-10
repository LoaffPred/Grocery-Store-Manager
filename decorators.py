"""Decorators

    For use within the project [Grocery-Store-Manager]


    decorators:
        @input_validator -> returns user input, else None
        - Compares user input vs accepted inputs and only allows accepted inputs

        @alpha_only -> returns user input, else None
        - Allows only alphabetic characters as input

        @num_only -> returns user input, else None
        - Allows only numbers as input

        @limit_input -> returns user input, else None
        - Allows only an input to be of a specific range

        @transition_pause -> returns None
        - Attempts to control and limit movement of outputs

        @print_header -> returns None
        - Prints a header before executing the function

"""


def input_validator(*args):
    def outer(func):
        def inner(self):
            a = func(self)
            if a != "" and a in args:
                return a
            else:
                print("Invalid Input. Allowed inputs are,", args)

        return inner

    return outer


def alpha_only(func):
    def inner(self):
        a = func(self)
        if a.isalpha():
            return a
        else:
            print("Invalid Input. Only alphabetic letters are allowed [a-zA-Z]")

    return inner


def num_only(func):
    def inner(self):
        a = func(self)
        try:
            if a.isdigit():
                return int(a)
            else:
                return float(a)
        except ValueError:
            print("Invalid input. Only numbers are allowed [0-9].")

    return inner


def limit_input(llimit, ulimit):
    def outer(func):
        def inner(self):
            a = func(self)
            if a and llimit <= a <= ulimit:
                return a
            else:
                print("Input a reasonable amount.")

        return inner

    return outer


def transition_pause(func):
    def inner(self):
        func(self)
        input("Press [enter] to proceed...")

    return inner


def print_header(header):
    def outer(func):
        def inner(self):
            print("====================>>> ", end="")
            for l in header:
                print(l + " ", end="")
            print("<<<====================")
            func(self)

        return inner

    return outer
