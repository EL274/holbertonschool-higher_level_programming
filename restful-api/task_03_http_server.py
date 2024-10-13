#!/usr/bin/python3

import http.server
import socketserver
import json


# Define the request handler class
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        # Define the different endpoints
        if self.path == "/":
            # Root endpoint: returns a simple message
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == "/data":
            # /data endpoint: returns a sample JSON dataset
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            # /status endpoint: returns an OK status
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())
        
        elif self.path == "/info":
            # /info endpoint: returns version info
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            # Any other endpoint: return 404
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Not Found"}
            self.wfile.write(json.dumps(error_message).encode())
    
    # Suppress the default logging
    def log_message(self, format, *args):
        return

# Set up the HTTP server
PORT = 8000
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
