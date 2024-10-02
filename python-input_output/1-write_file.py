#!/usr/bin/python3
"""Defines a function writes text file and returns the number of characters written."""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
