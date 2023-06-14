#!/usr/bin/python3

"""This module inserts a line of text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file, after each
    line containing a specific string using with statement"""
    with open(filename, encoding="UTF8") as my_file:
        lines = my_file.readlines()

    lines_container = []

    for line in lines:
        lines_container.append(line)

        if search_string in line:
            lines_container.append(new_string)

    with open(filename, "w", encoding="UTF8") as my_file:
        my_file.writelines(lines_container)
