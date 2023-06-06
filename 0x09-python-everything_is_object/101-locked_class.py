#!/usr/bin/python3
"""This module prevent the user from dynamically creating
new instance attributes, except if the new instance attribute
is called first_name"""


class LockedClass:
    """A class that prevent user from creating new instance attributes
    except if the new instance attribute called first_name"""

    __slots__ = ['first_name']
    """Attribute is used to explicitly define the allowed
    instance attributes."""

    def __init__(self, first_name=""):
        """Initialize the LockedClass object."""
        self.first_name = first_name
