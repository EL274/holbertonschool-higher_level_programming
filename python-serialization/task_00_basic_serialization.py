#!/usr/bin/env python3
"""Module for serializing and saving Python dictionaries to JSON files."""


import json


def serialize_and_save_to_file(data, filename):
    """serialize and save data to the specified file pass"""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")


def load_and_deserialize(filename):
    """load and deserialize data from the specified file pass"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred while loading data from {filename}: {e}")
        return None
