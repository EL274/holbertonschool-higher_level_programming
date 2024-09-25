#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle"""


Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for Square that inherits from Rectangle
    with methods for area and string representation."""

    def __init__(self, size):
        """Initializes Square instance"""
        self.__size = self.integer_validator(size)

    def integer_validator(self, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("size must be a positive integer")
        return value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """String representation of Square"""
        return f"[Square] {self.__size}/{self.__size}"
