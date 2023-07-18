#!/usr/bin/python3

"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """This class is inherits from list"""

    def print_sorted(self):
        """Function that prints a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
