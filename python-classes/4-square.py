#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size and public instance methods."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
