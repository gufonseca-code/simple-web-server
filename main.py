import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Return a page to HTTP requests
    """

    page = """
<html>
    <body>
        <p>Hello World!</p>
    </body>
</html>
"""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.page)))
        self.end_headers()
        self.wfile.write(self.page.encode())

def main():
    serverAddress = ("", 8080)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()