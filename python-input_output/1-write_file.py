#!/usr/bin/python3
"""Defines a function writes text file and returns number of characters"""


def write_file(filename="", text=""):
    """Writes text file and returns number of characters"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
