#!/usr/bin/python3
"""Définit une fonction qui renvoie les attributs et méthodes d'un objet."""


def lookup(obj):
    """Renvoie la liste des attributs et méthodes disponibles d'un objet."""
    return dir(obj)
