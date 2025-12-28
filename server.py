from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

port = int(os.environ.get('PORT', 8080))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

print(f"Starting server on port {port}")
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
