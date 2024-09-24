#!/usr/bin/python3
"""defines class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Class for rectangle that inherits from BaseGeometry with print() and str() ability"""
    def __init__(self, width, height):
        """Initializes Rectangle instance with width and height after validation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """String representation of Rectangle"""
        str_rep = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return str_rep

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height
