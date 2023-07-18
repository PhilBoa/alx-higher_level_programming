#!/usr/bin/python3

"""This module defines a function is_same_class() that
returns True if the object is exactly an instance of the
specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly
    an instance of the specified class ; otherwise False"""

    return type(obj) == a_class
