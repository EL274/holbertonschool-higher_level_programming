#!/usr/bin/python3
"""defines function that counts number of lines read from file"""



def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
  