import http.server
from urllib.parse import urlparse, parse_qs
import datetime
import json

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    time = datetime.datetime.now().isoformat()
    url = urlparse(self.path)
    path = url.path
    query = parse_qs(url.query)

    if url.path == '/ping':
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()

      response = 'pong!'
      
    elif url.path == '/api/time':
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
    
    elif url.path == '/api/best':
      if 'name' in query:
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = query['name'][0] + ' is the best minion!'
      
      else:
        self.send_response(404)
        self.end_headers()
        response = ''

    else:
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
  
      response = 'Bananas!'
    
    print(response)
    self.wfile.write(bytes(response, 'utf-8'))


  def do_POST(self):

    if self.path == '/api/log':
      if self.headers['Content-type'] == 'application/json':
        dataLength = int(self.headers['Content-Length'])
        rawData = self.rfile.read(dataLength)
        data = json.loads(rawData)
        if 'text' in data:
          self.send_response(200)
          self.send_header('Content-type', 'application/json')
          self.end_headers()

          response = json.dumps({'status': 'OK', 'message': data['text']})

      else:     
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response = 'Bananas!'
    
    print(response)
    self.wfile.write(bytes(response, 'utf-8'))

server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()