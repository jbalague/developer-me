import http.server
import datetime
import json

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    time = datetime.datetime.now().isoformat()
    if self.path == '/ping':
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()

      response = 'pong!'
      
    elif self.path == '/api/time':
      if 'Accept' in self.headers:
        if self.headers['Accept'] == 'application/json':
          self.send_response(200)
          self.send_header('Content-type', 'application/json')
          self.end_headers()

          response = json.dumps({'time': time}) 
        
        else:
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()

          response = json.dumps(time) 
        
    else:
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()

      response = 'Bananas!'
    
    print(response)
    self.wfile.write(bytes(response, 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()