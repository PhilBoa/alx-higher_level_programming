#!/usr/bin/python3

"""This module defines a class MyInt that inherits int."""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if
    it's possible, it Raise a TypeError exception if the
    object can't have new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
