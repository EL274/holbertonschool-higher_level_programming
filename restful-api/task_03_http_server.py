#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


"""Classe qui gère les requêtes HTTP"""
class SimpleAPIHandler(BaseHTTPRequestHandler):
    
    # Gère les requêtes GET
    def do_GET(self):
        # Gérer la route principale "/"
        if self.path == "/":
            self.send_response(200)  # Réponse HTTP 200 OK
            self.send_header("Content-type", "text/plain")  # Définir le type de contenu
            self.end_headers()  # Fin des en-têtes
            self.wfile.write(b"Hello, this is a simple API!")  # Corps de la réponse
        
        # Gérer la route "/data"
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Les données à renvoyer en JSON
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())  # Convertir dict en JSON
        
        # Gérer la route "/status"
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status_data = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status_data).encode())
        
        # Gérer les routes non définies
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_data = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error_data).encode())

# Fonction pour démarrer le serveur HTTP
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting http server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
