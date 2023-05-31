#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or \
                (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def __str__(self):
        """Return a string representation of the square."""
        if self.__size == 0:
            return ""
        else:
            square_str = ""
            for i in range(self.__position[1]):
                square_str += "\n"
            for j in range(self.__size):
                square_str += " " * self.__position[0] + "#"\
                        * self.__size + "\n"

        return square_str

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

    @property
    def position(self):
        """Retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute."""
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
