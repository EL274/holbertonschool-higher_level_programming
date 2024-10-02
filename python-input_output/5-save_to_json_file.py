#!/usr/bin/python3
"""defines function writes json representation an object"""


def save_to_json_file(my_obj, filename):
    """write representation json an object to file"""
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
