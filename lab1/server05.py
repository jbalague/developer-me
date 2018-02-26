import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    if self.path == '/ping':
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()

      response = 'pong!'
      
    else:
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()

      response = '<h1>Bello bol!</h1>'
      response = response + '<br>' + self.command + ' ' + self.path + '<br>'
      for header in self.headers:
        response = response + '<br>' + header + ': ' + self.headers[header]
    
    print(response)
    self.wfile.write(bytes(response, 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()