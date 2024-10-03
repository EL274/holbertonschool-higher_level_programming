#!/usr/bin/python3
"""Module for serializing and saving Python dictionaries to JSON files."""


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a specified JSON file."""
    import json
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")


def load_and_deserialize(filename):
    """Loads and deserializes JSON data from a specified file."""
    try:
        with open(filename, 'r') as file:
            return json.loads(file)
    except Exception as e:
        print(f"An error occurred while loading data from {filename}: {e}")
        return None
