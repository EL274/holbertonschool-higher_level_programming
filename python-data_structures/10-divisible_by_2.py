#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    # Utiliser {:s} pour une chaîne et conditionner correctement le texte
    print("{:d} is {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1  # Incrémentation ici est correcte
