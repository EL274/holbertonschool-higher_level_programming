#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""
    
    def __init__(self, width, height):
        """Initialize width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height
