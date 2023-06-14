#!/usr/bin/python3

"""This module creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
