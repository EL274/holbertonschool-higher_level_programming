from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Root endpoint


@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Serve JSON data for users


@app.route('/data')
def get_users():
    return jsonify(users)

# Status endpoint


@app.route('/status')
def status():
    return jsonify({"status": "OK"})

# Get details of a specific user by username


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Add a new user via POST request


@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.json
    username = user_data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "name": user_data.get('name'),
        "age": user_data.get('age'),
        "city": user_data.get('city')
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

# Run the Flask server


if __name__ == "__main__":
    app.run(debug=True)
