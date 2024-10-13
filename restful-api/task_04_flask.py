#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'votre_cle_secrete'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Utilisateurs avec mots de passe hachés et rôles
users = {
    "admin": {
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    },
    "user": {
        "password": generate_password_hash("user_password"),
        "role": "user"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not verify_password(username, password):
        return jsonify({"msg": "Bad credentials"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return jsonify({"msg": f"Hello, {user}! This is a protected route."})


@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    user = get_jwt_identity()
    if users[user]['role'] != 'admin':
        return jsonify({"msg": "Admins only!"}), 403
    return jsonify({"msg": f"Welcome, {user}. You are an admin!"})


if __name__ == '__main__':
    app.run(debug=True)
