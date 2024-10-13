#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Get all users (JSON data)
@app.route('/data')
def get_users():
    return jsonify(users)

# Get status
@app.route('/status')
def status():
    return "OK"

# Get user by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Add a new user (POST request)
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]})

if __name__ == '__main__':
    app.run(debug=True)
