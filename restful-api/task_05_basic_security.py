#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Clé secrète pour JWT
app.config['JWT_SECRET_KEY'] = 'votre_cle_secrete'

# Initialisation des extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}

roles = {
    "admin": "admin",
    "user": "user"
}
"""Authentification of users"""


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

# Route protégée par l'authentification HTTP Basic


@app.route('/basic_protected')
@auth.login_required
def basic_protected():
    return jsonify(message=f"Bienvenue, {auth.current_user()}!"), 200


"""Route de login pour générer un token JWT"""


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity={'username': username, "role": user['role']}
            )
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt_protected')
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


"""Route avec contrôle d'accès basé sur les rôles"""


@app.route('/admin_only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
