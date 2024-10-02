def pascal_triangle(n):
    # Si n est inférieur ou égal à 0, retourner une liste vide
    if n <= 0:
        return []

    # Initialisation du triangle de Pascal avec la première ligne
    triangle = [[1]]

    # Construction du triangle ligne par ligne
    for i in range(1, n):
        # Récupérer la dernière ligne du triangle pour construire la nouvelle
        prev_row = triangle[-1]
        # Commencer chaque nouvelle ligne avec 1
        new_row = [1]
        
        # Ajouter les sommes des éléments adjacents de la ligne précédente
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        # Terminer la nouvelle ligne avec 1
        new_row.append(1)
        
        # Ajouter la nouvelle ligne au triangle
        triangle.append(new_row)

    return triangle

# Exemple d'utilisation
print(pascal_triangle(5))

