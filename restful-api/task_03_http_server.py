from http.server import HTTPServer,BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('Hello, this is a simple API!'.encode())

        
def main():
    PORT = 8000
    server = HTTPServer(('' ,PORT), SimpleHTTPRequestHandler)
    print('server running on port %s' % PORT)
    server.serve-forever()


if _name_ == '_main_':
    main()
