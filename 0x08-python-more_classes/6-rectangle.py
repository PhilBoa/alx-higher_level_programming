#!/usr/bin/python3

"""This module defines the Rectangle class."""


class Rectangle:
    """This class represents a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def my_print(self):
        """Prints in stdout the Rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for i in range(self.__height):
                print("#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += "#" * self.__width
                if i != self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """Return a string representation of the Rectangle that
        can be used to recreate a new instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints in stdout the deletef Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
