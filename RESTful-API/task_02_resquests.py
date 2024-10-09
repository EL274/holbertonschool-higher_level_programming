#!/usr/bin/python3


import requests

def fetch_and_print_posts():
    # URL de l'API JSONPlaceholder pour récupérer les posts
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Envoie une requête GET pour récupérer les posts
    response = requests.get(url)
    
    # Affiche le code de statut de la réponse
    print(f"Status Code: {response.status_code}")
    
    # Si la requête a réussi (status_code == 200)
    if response.status_code == 200:
        # Convertir la réponse en JSON
        posts = response.json()
        
        # Parcourir les posts et afficher les titres
        for post in posts:
            print(post['title'])

# Tester la fonction
fetch_and_print_posts()

