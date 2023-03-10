"""
Provides functions that deal with file manipulation,
specifically JSON files.
"""

import json
from os import getcwd, path


def read_json(filename):
    with open(path.join(getcwd(), filename), "r") as file:
        data = json.load(file)

    return data


def write_json(filename, data):
    with open(path.join(getcwd(), filename), "w") as file:
        json.dump(data, file, indent=4)


def get_data(filename, data):
    try:
        return read_json(filename)
    except:
        write_json(filename, data)
        return read_json(filename)
