#!/usr/bin/python3


import requests

def fetch_and_print_posts():
    """URL de l'API JSONPlaceholder pour récupérer les posts"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    """Envoie une requête GET pour récupérer les posts"""
    response = requests.get(url)
    
    """Affiche le code de statut de la réponse"""
    print(f"Status Code: {response.status_code}")
    
    """Si la requête a réussi (status_code == 200)"""
    if response.status_code == 200:
        """Convertir la réponse en JSON"""
        posts = response.json()
        
        """Parcourir les posts et afficher les titres"""
        for post in posts:
            print(post['title'])


import csv

def fetch_and_save_posts():
    """ URL de l'API JSONPlaceholder pour récupérer les posts"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    """Envoie une requête GET pour récupérer les posts"""
    response = requests.get(url)
    
    """Si la requête a réussi (status_code == 200)"""
    if response.status_code == 200:
        """Convertir la réponse en JSON"""
        posts = response.json()
        
        """Préparer les données sous forme d'une liste de dictionnaires"""
        post_list = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        """Ouvrir un fichier CSV en mode écriture"""
        with open('posts.csv', mode='w', newline='') as file:
            """Créer un objet DictWriter pour écrire dans le fichier CSV"""
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            
            """ Écrire l'en-tête (noms des colonnes)"""
            writer.writeheader()
            
            """ Écrire les données dans le fichier"""
            writer.writerows(post_list)
