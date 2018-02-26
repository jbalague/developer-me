import http.server
import datetime
import json
import sys

ADDRESS = '127.0.0.1'
PORT = int(sys.argv[1])

USERS = {
  'admin': 'secret',
  'user1': 'secret'
}

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    
    if self.path == '/api/time.text':
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
      response = bytes(datetime.datetime.now().isoformat(), 'utf-8')
    elif self.path == '/api/time.json':
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      r = {}
      r['server'] = PORT
      r['timestamp'] = datetime.datetime.now().isoformat()
      response = bytes(json.JSONEncoder().encode(r), 'utf-8')

    else:
      self.send_response(404)
      self.end_headers()
      response = bytes('', 'utf-8')

    self.wfile.write(response)

  def do_POST(self):
    
    response = ''
    code = 200
    if self.path == "/api/login":
      try:
        length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(length))
        if data['password'] == USERS[data['username']]:
          response = {}
          response['result'] = 'success'
          response['data'] = {}
          response['data']['token'] = '1234567890'
        else:
          raise Exception('Invalid username or password') 
      except:
        code = 403
        response = {}
        response['result'] = 'error'
        response['data'] = {}
        response['data']['message'] = 'Invalid username and/or password'
    else:
      dataLength = int(self.headers['Content-Length'])
      data = self.rfile.read(dataLength)
      if self.headers['Content-type'] == 'application/json':
        print('POST json data: %s' % json.loads(data))
        d = json.loads(data)
        if 'bb' in d:
          print(d['bb'])

      else:
        print('POST data: %s' % data)
    self.send_response(code)
    self.end_headers()
    self.wfile.write(bytes(response, 'utf-8'))


server = http.server.HTTPServer((ADDRESS, PORT), RequestHandler)
try:
  print('Listening at port %d' % PORT)
  server.serve_forever()
except KeyboardInterrupt:
  print('\nServer closing...\n')
finally:
  server.server_close()
