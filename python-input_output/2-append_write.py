#!/usr/bin/python3
"""defines function to append string text file"""

def append_write(filename="", text=""):
    """append string in text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
