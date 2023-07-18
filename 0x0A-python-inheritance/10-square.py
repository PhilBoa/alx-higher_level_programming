#!/usr/bin/python3

"""This module defines Rectangle class that inherits
a class BaseGeometry with public instance method area and
integer_validator."""


class BaseGeometry(object):
    """Class BaseGeometry with public instance method area
    and integer_validator that validates value: if value is
    not an integer: raise a TypeError exception, if value is
    less or equal to 0: raise a ValueError exception."""

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectange that inherits BaseGeometry with
    Instantiation with width and height that get validated
    by integer_validator"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class Square that inherits Rectangle Instantiation
    with size and get validated with integer_validator"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
