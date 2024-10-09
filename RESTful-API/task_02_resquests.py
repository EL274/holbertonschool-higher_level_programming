#!/usr/bin/python3

import csv
import requests

def fetch_and_print_posts():
    """Récupère et affiche les posts de JSONPlaceholder"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Récupère et sauvegarde les posts de JSONPlaceholder dans un CSV"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        post_list = [{'id': p['id'], 'title': p['title'], 'body': p['body']} 
                     for p in posts]
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(post_list)

