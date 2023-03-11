
def print_header(func):
    def wrapper(text):
        func()

    return wrapper