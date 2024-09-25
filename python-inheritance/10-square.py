#!/usr/bin/python3
"""defines class square inherits rectangle"""


Rectangle = _import_('9-rectangle').Rectangle


class Shape(rectangle):
    def __init__(self, size):
        self.__integer_validator(size)
        self.__size = size

    def __integer_validator(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be a positive integer")

    def area(self):
        raise NotImplementedError("The area() method must be implemented by subclasses")
