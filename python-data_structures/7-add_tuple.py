#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # On complète les tuples avec des zéros si nécessaire
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # On additionne les éléments correspondants
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
