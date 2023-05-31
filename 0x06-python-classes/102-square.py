#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize the Square object."""
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __eq__(self, num):
        """Compares two Square instances for equality
        based on their areas."""
        if isinstance(num, Square):
            return self.area() == num.area()
        return NotTrue

    def __ne__(self, num):
        """Compares two Square instances for nequality
        based on their areas."""
        if isinstance(num, Square):
            return self.area() != num.area()
        return NotTrue

    def __gt__(self, num):
        """Compares two Square instances to check if the
        first square has a greater area."""
        if isinstance(num, Square):
            return self.area() > num.area()
        return NotTrue

    def __ge__(self, num):
        """Compares two Square instances for equality or
        first greater than second based on their areas."""
        if isinstance(num, Square):
            return self.area() >= num.area()
        return NotTrue

    def __lt__(self, num):
        """Compares two Square instances to check if first
        less than second based on area."""
        if isinstance(num, Square):
            return self.area() < num.area()
        return NotTrue

    def __le__(self, num):
        """Compares two Square instances for equality or
        first less than second based on their areas."""
        if isinstance(num, Square):
            return self.area() <= num.area()
        return NotTrue
