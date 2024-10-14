#!/usr/bin/python3

import csv
import requests


def fetch_and_print_posts():
    # Récupère et affiche les posts de JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return

    print(f"Status Code: {response.status_code}")
    try:
        posts = response.json()
    except ValueError:
        print("Erreur : réponse non valide, impossible de décoder le JSON.")
        return

    for post in posts:
        print(post['title'])


def fetch_and_save_posts():
    '# Récupère et sauvegarde les posts de JSONPlaceholder dans un CSV'
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return

    try:
        posts = response.json()
    except ValueError:
        print("Erreur : réponse non valide, impossible de décoder le JSON.")
        return

    post_list = [{'id': p['id'], 'title': p['title'], 'body': p['body']}
                 for p in posts]
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(post_list)
    print("Posts have been saved to posts.csv.")
