import json from http.server import BaseHTTPRequestHandler, HTTPServer


# Classe qui gère les requêtes HTTP
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Méthode pour gérer les requêtes GET
    def do_GET(self):
        # Vérification du chemin de la requête
        if self.path == '/':
            # Répondre avec un message simple pour la page d'accueil
            self.send_response(200)  # Réponse avec le code 200 OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!")
        elif self.path == '/data':
            # Répondre avec des données JSON
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)  # Réponse OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            # Répondre avec un statut de l'API
            self.send_response(200)  # Réponse OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")  # Réponse avec statut OK
        else:
            # Gérer les chemins non définis (404 Not Found)
            self.send_response(404)  # Réponse 404
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(
                b"404 Not Found: The requested endpoint was not found on this server."
            )


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http server on port {port}...')
    httpd.serve_forever()  # Boucle pour écouter les requêtes


if __name__ == '__main__':
    run()
