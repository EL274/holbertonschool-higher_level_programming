#!/usr/bin/python3
"""defines function writes python module name"""
import json
def serialize_and_save_to_file(data, filename):

    
    """Serializes Python dictionary and saves specified file in JSON format."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")
def load_and_deserialize(filename):
    """Loads and deserializes JSON data specified file Python dictionary."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred while loading data from {filename}: {e}")
        return None
