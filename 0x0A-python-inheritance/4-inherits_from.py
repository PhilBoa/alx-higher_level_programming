#!/usr/bin/python3

"""This module defines a function that returns
True if the object is an instance of a class that inherited
(directly or indirectly) ; otherwise
False."""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly); otherwise
    False."""

    return issubclass(type(obj), a_class) and type(obj) != a_class
