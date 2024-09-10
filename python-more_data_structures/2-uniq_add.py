#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Ajoute tous les entiers uniques d'une liste (une seule fois pour chaque entier)."""
    result = 0  # Initialiser la variable qui stocke la somme
    for x in set(my_list):  # Convertir la liste en un ensemble pour supprimer les doublons
        result += x  # Ajouter chaque entier unique à la somme
    return result  # Retourner la somme des entiers uniques
