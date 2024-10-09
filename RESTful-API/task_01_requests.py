#!/usr/bin/python3


import requests
import json

# URL de l'API
url = "https://jsonplaceholder.typicode.com/posts"

# 1. Faire une requête GET pour récupérer les posts
response = requests.get(url)

"""Vérifier si la requête a réussi (code de statut 200)"""
if response.status_code == 200:
    # Afficher les posts (JSON formaté)
    posts = response.json()
    print("Liste des posts :")
    print(json.dumps(posts, indent=4))
else:
    print(f"Erreur lors de la récupération des posts : {response.status_code}")

"""Faire une requête POST pour envoyer des données"""
new_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response_post = requests.post(url, data=new_post)

# Vérifier si la requête POST a réussi (code de statut 201 pour une création)
if response_post.status_code == 201:
    # Afficher la réponse du serveur après la création du nouveau post
    created_post = response_post.json()
    print("\nPost créé :")
    print(json.dumps(created_post, indent=4))
else:
    print(f"Erreur lors de la création du post : {response_post.status_code}")
