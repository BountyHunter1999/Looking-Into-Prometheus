import http.server
import random
import time
from prometheus_client import start_http_server, Counter, Gauge

REQUESTS = Counter("hello_worlds_total", "Hello Worlds requested.")
EXCEPTIONS = Counter("hello_world_exceptions_total", "Exceptions serving Hello World.")
INPROGRESS = Gauge("hello_worlds_inprogress", "Number of Hello Worlds in progress.")
LAST = Gauge("hello_world_last_time_seconds", "The Last time a Hello World was served.")


class MyHandler(http.server.BaseHTTPRequestHandler):
    # @EXCEPTIONS.count_exceptions()
    @INPROGRESS.track_inprogress()
    def do_GET(self):
        REQUESTS.inc()
        # INPROGRESS.inc()
        with EXCEPTIONS.count_exceptions():
            if random.random() < 0.2:
                raise Exception
        self.send_response(200)

        self.end_headers()
        self.wfile.write(b"Hello World!!")
        # use as `time() - hello_world_last_time_seconds`
        # LAST.set(time.time())
        LAST.set_to_current_time()  # set the guage to current time stamp
        # INPROGRESS.dec()


if __name__ == "__main__":
    start_http_server(8000)
    # allow external access with 0.0.0.0
    server = http.server.HTTPServer(("0.0.0.0", 8001), MyHandler)
    print("Starting server on port 8001, prometheus related logs at 8000")
    server.serve_forever()
