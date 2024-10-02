#!/usr/bin/python3
"""defines function to read text file and prints to stdout"""


def read_file(filename=""):
    """reads text file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
