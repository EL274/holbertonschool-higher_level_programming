#!/usr/bin/python3
"""defines function return Json in object"""


def to_json_string(my_obj):
    """return representation json an object"""
    import json 
    return json.dumps(my_obj)
