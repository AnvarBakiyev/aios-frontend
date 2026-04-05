import http.server
import socketserver
import os

PORT = int(os.environ.get('PORT', 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or not self.path.endswith(('.js','.css','.png','.ico','.json')):
            self.path = '/index.html'
        return super().do_GET()
    def log_message(self, format, *args):
        pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f'AI Corporate OS Frontend serving on port {PORT}')
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()
