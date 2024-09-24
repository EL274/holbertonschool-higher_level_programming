#!/usr/bin/python3
"""
Defines a function to check if an object is an instance of a class
that is a subclass (direct or indirect) of the specified class.
"""

def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited 
    (directly or indirectly) from the specified class; otherwise False.
    """
    
    # Check if obj is an instance of a subclass of a_class but not a_class itself
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
