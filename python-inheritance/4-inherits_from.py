#!/usr/bin/python3
"""defines function to see if object is an instance of a class
that is a subclass of the specified class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited 
    (directly or indirectly) from the specified class; otherwise False"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
