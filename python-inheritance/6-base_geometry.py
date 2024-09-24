#!/usr/bin/python3
"""Defines class BaseGeometry with a public instance method for area."""


class BaseGeometry:
    """Class with a public instance method to raise an exception."""
    
    def area(self):
        """Raises an exception to indicate the method is not implemented."""
        raise Exception("area() is not implemented")
