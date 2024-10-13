#!/usr/bin/python3
"""A simple API using Python with Flask
this function allows to make a request and add new-user"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"

"""returns the list of all usernames"""


@app.route('/data')
def username():
    return jsonify(list(users.keys()))


# Get status
@app.route('/status')
def status():
    return ("OK")


"""Get user by username"""
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Add a new user (POST request)


@app.route('/add_user', methods=['POST'])
def add_user():
    new_user= request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "User is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
