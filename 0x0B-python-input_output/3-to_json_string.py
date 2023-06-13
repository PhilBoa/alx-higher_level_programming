#!/usr/bin/python3

"""This module returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
