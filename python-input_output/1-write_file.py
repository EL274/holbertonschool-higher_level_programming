#!/usr/bin/python3
"""Defines a function that writes text to a file and returns  number""" 


def write_file(filename="", text=""):

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
