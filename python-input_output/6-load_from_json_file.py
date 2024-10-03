#!/usr/bin/python3
"""defines functions creates an object from json"""


def load_from_json_file(filename):
    """creates an abject from json"""
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
