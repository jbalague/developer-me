import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    self.wfile.write(bytes('<h1>Bello bol!</h1>', 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()