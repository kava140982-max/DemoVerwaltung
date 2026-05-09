# run_server.py
# Einfacher Python-HTTP-Server zum Starten der Demo
# °KaVa090526

import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Demo-Server läuft auf http://localhost:{PORT}")
    print("°KaVa090526")
    httpd.serve_forever()
