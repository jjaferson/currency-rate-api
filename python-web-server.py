import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
from euro import Euro
from currency import CurrencyType

class StaticServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        euro = Euro()
        euro.add_currency(CurrencyType.REAL)
        self.wfile.write(euro.toJson().encode("utf8"))



def run(server_class=HTTPServer, handler_class=StaticServer, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting Server on port {}'.format(port))
    httpd.serve_forever()

run()