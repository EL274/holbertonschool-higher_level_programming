#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Si le tuple_a a moins de deux éléments, on le complète avec des zéros
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:  # Si tuple_a a un seul élément
            tuple_a = (tuple_a[0], 0)  # On ajoute un 0 en deuxième position
        else:  # Si tuple_a est vide
            tuple_a = (0, 0)  # On met deux zéros

    # Si le tuple_b a moins de deux éléments, on le complète avec des zéros
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:  # Si tuple_b a un seul élément
            tuple_b = (tuple_b[0], 0)  # On ajoute un 0 en deuxième position
        else:  # Si tuple_b est vide
            tuple_b = (0, 0)  # On met deux zéros

    # On additionne le premier élément de chaque tuple et le deuxième élément de chaque tuple
    sum_first_elements = tuple_a[0] + tuple_b[0]
    sum_second_elements = tuple_a[1] + tuple_b[1]

    # On retourne un nouveau tuple avec les résultats des additions
    return (sum_first_elements, sum_second_elements)
