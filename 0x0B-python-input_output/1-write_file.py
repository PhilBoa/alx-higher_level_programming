#!/usr/bin/python3

"""This module is about writing a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file encoded with
    (UTF8) and returns the number of characters written
    using with statement"""
    with open(filename, "w", encoding="UTF8") as my_file:
        my_file.write(text)
        return len(text)
