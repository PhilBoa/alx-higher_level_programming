#!/usr/bin/python3

"""This module creates a class Student that defines a student
and retrieves a dictionary representation of a Student instance"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle of n.
    """
    triangle = []

    if n <= 0:
        return triangle

    row = [1]
    triangle.append(row)

    for i in range(1, n):
        curr_row = [1]

        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            curr_row.append(element)

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
