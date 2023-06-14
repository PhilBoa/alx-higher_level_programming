#!/usr/bin/python3

"""This module details a Python class-to-JSON function."""


def class_to_json(obj):
    """A function that returns the dictionary represntation of a simple data structure."""

    return obj.__dict__
