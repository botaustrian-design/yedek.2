import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Sunucu http://localhost:{PORT} adresinde çalışıyor...")
    httpd.serve_forever()

