#!/usr/bin/python3
"""defines class Square that inherits from Rectangle"""


class Square:
     """class for square that inherits from Rectangle
    with method for area and string representation"""
     
    def __init__(self, size):
        """initializes Square instance"""
        self.__size = self.integer_validator(size)

    def integer_validator(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("size must be a positive integer")
        return value

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation of Square"""
        return f"[Square] {self.__size}/{self.__size}"

    def print(self):
        print(self.__str__())
