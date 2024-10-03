#!/usr/bin/python3
"""defines function returns description data structure"""


def class_to_json(obj):
    """return description data structure"""
    return obj.__dict__
