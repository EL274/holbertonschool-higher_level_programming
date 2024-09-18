#!/usr/bin/python3
class Square:
"""defines class with instantiated and validated private instance attribute
and public instance method."""

    def __init__(self, size=0):
        self.__size = size

    @property
def size(self):
        return(self.__size)

    @size.setter
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
