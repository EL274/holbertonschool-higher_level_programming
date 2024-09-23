#!/usr/bin/python3
"""Defines a function that checks if an object is exactly an instance of a specified class."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.
    Otherwise, returns False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
