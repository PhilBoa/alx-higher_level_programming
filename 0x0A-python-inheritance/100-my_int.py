#!/usr/bin/python3

"""This module defines a class MyInt that inherits int."""


class MyInt(int):
    """This class is inherits int, MyInt has == and !=
    operators inverted"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
