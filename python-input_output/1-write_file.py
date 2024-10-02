#!/usr/bin/python3
"""
Defines a function that writes text to a file and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes text to a file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
