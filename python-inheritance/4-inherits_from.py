#!/usr/bin/python3
"""Defines a function to see an object is an instance of a class or the specified class"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited the specified class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
