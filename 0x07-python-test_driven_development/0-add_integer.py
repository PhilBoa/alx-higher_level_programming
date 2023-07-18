#!/usr/bin/python3

"""This module creates addition function."""


def add_integer(a, b=98):
    """Function that adds two numbers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
        if isinstance(b, float):
            b = int(b)
    return a + b
