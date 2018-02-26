import http.server
import urllib.request
import random

ADDRESS = '127.0.0.1'
PORT = 3333
WORKERS = ['3341', '3342', '3343']

class requestHandler(http.server.BaseHTTPRequestHandler):
  
  def do_GET(self):
    
    workerPort = random.choice(WORKERS)
    workerUrl = 'http://127.0.0.1:' + workerPort + self.path
    print('Forwarding request to %s' % workerUrl)
    response = bytes('', 'utf-8')
    try:
      request = urllib.request.urlopen(workerUrl)
      self.send_response(request.code)
      for header in request.getheaders():
        if header[0] == 'Content-type':
          self.send_header(header[0], header[1])
      self.end_headers()
      response = request.read()
    except:
      self.send_response(504)
      self.end_headers()
    finally:
      self.wfile.write(response)

server = http.server.HTTPServer((ADDRESS, PORT), requestHandler)
try:
  print('Load balancer listening at port %d' % PORT)
  server.serve_forever()
except KeyboardInterrupt:
  print('\nServer closing...\n')
finally:
  server.server_close()