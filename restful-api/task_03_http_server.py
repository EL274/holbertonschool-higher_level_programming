#!/usr/bin/python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


"""Classe qui gère les requêtes HTTP"""


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Gère les requêtes GET"""
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())
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
