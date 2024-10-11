from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Réponse pour la racine de l'API
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode())

        elif self.path == '/status':
            # Réponse pour l'endpoint /status
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('OK'.encode('utf-8'))

        elif self.path == '/data':
            # Prépare les données JSON
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Convertit les données en JSON
            json_data = json.dumps(data)
            # Définit le code de réponse et les en-têtes
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Envoie les données JSON en réponse
            self.wfile.write(json_data.encode('utf-8'))

        else:
            # Gestion des erreurs pour les chemins non définis
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            error_message = {
                "error": "404 Not Found", "message": "error"
            }
            self.wfile.write(json.dumps(error_message).encode('utf-8'))


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), echoHandler)
    print('server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
