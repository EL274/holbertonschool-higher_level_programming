#!/usr/bin/python3

import csv
import requests

def fetch_and_print_posts():
    # Fetch and print posts from JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
        return

    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
    else:
        print(f"Error: unexpected status {response.status_code}")
        return

    try:
        posts = response.json()
    except ValueError:
        print("Error: invalid response, unable to decode JSON.")
        return

    if isinstance(posts, list):
        for post in posts:
            print(post['title'])
    else:
        print("Error: JSON data is not a list.")
    

def fetch_and_save_posts():
    # Fetch and save posts from JSONPlaceholder to a CSV
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
        return

    try:
        posts = response.json()
    except ValueError:
        print("Error: invalid response, unable to decode JSON.")
        return

    if isinstance(posts, list):
        post_list = [{'id': p['id'], 'title': p['title'], 'body': p['body']}
                     for p in posts]
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(post_list)
        print("Posts have been saved to posts.csv.")
    else:
        print("Error: JSON data is not a list.")
