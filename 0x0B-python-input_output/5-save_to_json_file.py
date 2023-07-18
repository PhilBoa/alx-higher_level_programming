#!/usr/bin/python3

"""This module writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using
    a JSON representation).

    Args:
        my_obj: The object to save as JSON.
        filename (str): The name of the file to save.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
