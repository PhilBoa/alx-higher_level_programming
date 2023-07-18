#!/usr/bin/python3

"""This module defines a class BaseGeometry with public
instance def area(self)."""


class BaseGeometry(object):
    """Class BaseGeometry with public instance def area(self)."""

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
