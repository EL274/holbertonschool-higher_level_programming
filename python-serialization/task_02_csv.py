#!/usr/bin/python3
"""defines function writes json data"""


import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Erreur : Le fichier {csv_filename} est introuvable.")
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False
