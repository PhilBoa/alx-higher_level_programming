#!/usr/bin/python3

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 3

    def calculate_perimeter(self):
        return 9 * self.side_length

