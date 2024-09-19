#!/usr/bin/python3
"""creates class Square with
private instance attribute size and public instance method"""

# Correct indentation with 4 spaces
class Square:
    """defines class with instantiated and validated private instance attribute
    and public instance method."""

    # Method indented properly
    def __init__(self, size=0):
        # 4-space indentation for instance variables
        self.__size = size

    # Property decorator indented correctly
    @property
    def size(self):
        # Correct use of whitespace after return statement
        return self.__size

    # Setter with proper indentation
    @size.setter
    def size(self, value):
        if type(value) is not int:
            # Properly indented block for error handling
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        # Assigning value with appropriate indentation
        self.__size = value

    # Area method with correct indentation
    def area(self):
        """calculates and returns current square area"""
        return self.__size * self.__size  # Proper whitespace around operators
