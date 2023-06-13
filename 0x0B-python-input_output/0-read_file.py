 #!/usr/bin/python3

"""This module details about reading a text file unicoded with
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout:
    using with statement"""
    with open(filename, encoding="UTF8") as my_file:
        lines = my_file.read().rstrip()
    print(lines)
