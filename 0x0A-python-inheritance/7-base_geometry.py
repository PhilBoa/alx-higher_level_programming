#!/usr/bin/python3

"""This module defines a class BaseGeometry with public
instance method area and integer_validator."""


class BaseGeometry(object):
    """Class BaseGeometry with public instance method area
    and integer_validator that validates value: if value is
    not an integer: raise a TypeError exception, if value is
    less or equal to 0: raise a ValueError exception."""

    def __init__(self):
        """Initialize the BaseGeometry instance."""
        pass

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
