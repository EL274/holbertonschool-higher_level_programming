#!/usr/bin/python3
"""Checks if object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) == a_class
