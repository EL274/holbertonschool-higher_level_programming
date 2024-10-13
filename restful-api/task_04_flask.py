from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from functools import wraps

app = Flask(__name__)

# Clé secrète pour JWT
app.config['JWT_SECRET_KEY'] = 'votre_cle_secrete_pour_jwt'

# Initialisation de HTTPBasicAuth et JWTManager
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Liste des utilisateurs avec mots de passe hachés et rôles
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

# Authentification de base
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# Décorateur pour vérifier les rôles
def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if users[current_user]["role"] != role:
                return jsonify({"msg": "Accès refusé, rôle insuffisant"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Route protégée avec authentification de base
@app.route('/protected-basic', methods=['GET'])
@auth.login_required
def protected_basic():
    return jsonify({"msg": f"Bienvenue, {auth.current_user()}! Vous avez accédé à une route protégée par authentification de base."})

# Route de login pour JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"msg": "Nom d'utilisateur ou mot de passe incorrect"}), 401
    
    # Créer un token JWT pour l'utilisateur
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Route protégée avec JWT
@app.route('/protected-jwt', methods=['GET'])
@jwt_required()
def protected_jwt():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Bienvenue, {current_user}! Vous avez accédé à une route protégée par JWT."})

# Route protégée par rôle (admin uniquement)
@app.route('/admin', methods=['GET'])
@jwt_required()
@role_required("admin")
def admin_only():
    return jsonify({"msg": "Bienvenue, admin! Vous avez accédé à une route réservée aux administrateurs."})

# Démarrage du serveur
if __name__ == '__main__':
    app.run(debug=True)
