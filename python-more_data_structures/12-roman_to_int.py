#!/usr/bin/python3
def roman_to_int(roman_string):
    # Vérification de la validité de l'entrée
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    # Dictionnaire des valeurs des chiffres romains
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Parcours de la chaîne de droite à gauche
    for char in reversed(roman_string):
        if char not in roman_to_int_map:
            return 0  # Si un caractère invalide est trouvé, retourne 0
        
        value = roman_to_int_map[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

