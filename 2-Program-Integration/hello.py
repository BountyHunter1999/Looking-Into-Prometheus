import http.server
from prometheus_client import start_http_server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World!!")


if __name__ == "__main__":
    start_http_server(8000)
    # allow external access with 0.0.0.0
    server = http.server.HTTPServer(("0.0.0.0", 8001), MyHandler)
    print("Starting server on port 8001, prometheus related logs at 8000")
    server.serve_forever()
