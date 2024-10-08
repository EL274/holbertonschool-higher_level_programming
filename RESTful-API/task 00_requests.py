# 1. Introduction
introduction = """
L'objectif de cet exercice est de comprendre les bases du protocole HTTP et de sa version sécurisée, HTTPS. 
Nous allons explorer les principales différences entre HTTP et HTTPS, analyser la structure des requêtes et réponses HTTP, 
et nous familiariser avec les méthodes HTTP courantes ainsi que les codes d'état les plus utilisés.
"""

# 2. Différences entre HTTP et HTTPS
differences_http_https = """
HTTP (Hypertext Transfer Protocol) est un protocole qui permet le transfert de données entre un navigateur web et un serveur. 
Cependant, il n’offre pas de protection des données, ce qui signifie que toute information échangée en HTTP peut être interceptée et lue par des tiers. 
HTTPS (Hypertext Transfer Protocol Secure), quant à lui, est une version sécurisée de HTTP. 
Il utilise des protocoles de chiffrement SSL/TLS pour garantir la confidentialité des données échangées et l'intégrité des informations, 
rendant le contenu inaccessible à d’éventuels espions.

Principales différences :
- Chiffrement : HTTPS chiffre les données échangées tandis que HTTP ne le fait pas.
- Certificat SSL/TLS : HTTPS requiert l’utilisation de certificats numériques pour établir une connexion sécurisée.
- Usage : HTTPS est généralement utilisé pour les sites web qui manipulent des informations sensibles comme les données de paiement ou les connexions utilisateurs.
"""

# 3. Structure des requêtes et réponses HTTP
structure_http = """
Une requête HTTP est composée de plusieurs éléments, chacun ayant une fonction spécifique :
- Méthode : Indique l'action que le client souhaite réaliser. Par exemple, GET pour récupérer des données ou POST pour envoyer des données au serveur.
- Chemin : L’URL demandée, c'est-à-dire la ressource à laquelle le client tente d'accéder (par exemple, /index.html).
- En-têtes : Ils contiennent des informations supplémentaires telles que le type de contenu (Content-Type), les cookies, les paramètres de l'utilisateur, etc.
- Corps : Ce champ est optionnel et utilisé principalement dans les requêtes POST ou PUT pour envoyer des données au serveur (par exemple, lors de la soumission d’un formulaire).

La réponse HTTP contient également des informations importantes :
- Code de statut : Un nombre à trois chiffres qui indique le résultat de la requête (par exemple, 200 pour une requête réussie, 404 pour une ressource non trouvée).
- En-têtes : Ils fournissent des informations sur le serveur, le type de contenu retourné, et d'autres détails.
- Corps : Il contient la ressource demandée, telle qu'une page HTML ou des données JSON.
"""

# 4. Méthodes HTTP courantes
http_methods = {
    "GET": "Récupérer des données depuis le serveur. Exemple : Charger une page web ou obtenir des données depuis une API.",
    "POST": "Envoyer des données au serveur. Exemple : Soumettre un formulaire ou créer un nouveau compte utilisateur.",
    "PUT": "Mettre à jour une ressource existante ou créer une nouvelle ressource si elle n'existe pas. Exemple : Mettre à jour les informations d'un utilisateur.",
    "DELETE": "Supprimer une ressource sur le serveur. Exemple : Supprimer un compte utilisateur ou une publication."
}

# 5. Codes d'état HTTP courants
http_status_codes = {
    200: "La requête a été exécutée avec succès. Exemple : Une page web est chargée correctement.",
    301: "La ressource demandée a été déplacée de manière permanente à une nouvelle URL. Exemple : Lorsqu'une page web est redirigée vers une autre adresse.",
    404: "La ressource demandée est introuvable. Exemple : L’utilisateur essaie d’accéder à une page qui n’existe pas.",
    500: "Une erreur interne au serveur a empêché la requête d’être exécutée. Exemple : Un bug côté serveur provoque une interruption du service."
}

# 6. Conclusion
conclusion = """
Cet exercice m'a permis de comprendre les différences essentielles entre HTTP et HTTPS, en particulier concernant la sécurité des données échangées. 
J'ai également appris à identifier la structure des requêtes et réponses HTTP, ainsi qu'à reconnaître les méthodes et les codes d'état les plus fréquents. 
Cela me donne une meilleure compréhension de la manière dont les navigateurs et les serveurs web communiquent.
"""

# Affichage des sections
print(introduction)
print(differences_http_https)
print(structure_http)

print("Méthodes HTTP courantes :")
for method, description in http_methods.items():
    print(f"- {method}: {description}")

print("\nCodes d'état HTTP courants :")
for code, description in http_status_codes.items():
    print(f"- {code}: {description}")

print(conclusion)

