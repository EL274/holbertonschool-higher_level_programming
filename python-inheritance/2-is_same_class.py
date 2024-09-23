#!/usr/bin/python3
"""Defines a function to see if an object is exactly an instance of class."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of class"""
    if type(obj) is a_class:
        return True
    else:
        return False
