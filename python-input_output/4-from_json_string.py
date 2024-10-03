#!/usr/bin/python3
"""defines function returns an object from json"""


import json


def from_json_string(my_str):
    """return an object from json"""
    return json.loads(my_str)
