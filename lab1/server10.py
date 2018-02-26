import http.server
import json
import datetime

ADDRESS = '127.0.0.1'
PORT = 8787


class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    if self.path == '/ping':
      self.sendPong()
    elif self.path == '/time':
      self.sendTime()
    elif self.path == '/time.text':
      self.sendTimeInText()
    elif self.path == '/time.json':
      self.sendTimeInJSON()
    else:
      self.sendError(404)


  def sendPong(self):

    response = {
      'code': 200,
      'headers': [
        {'name': 'Content-type', 'value': 'text/plain'},
      ],
      'body': 'Pong!'
    }
    self.send(response)


  def sendTime(self):

    if 'Accept' in self.headers:
      if self.headers['Accept'] == 'application/json':
        self.sendTimeInJSON()
      elif self.headers['Accept'] == 'text/plain':
        self.sendTimeInText()
      else:
        self.sendError() 
    else:
      self.sendError() 


  def sendTimeInText(self):

    response = {
      'code': 200,
      'headers': [
        {'name': 'Content-type', 'value': 'text/plain'},
      ],
      'body': datetime.datetime.now().isoformat()
    }
    self.send(response)


  def sendTimeInJSON(self):

    response = {
      'code': 200,
      'headers': [
        {'name': 'Content-type', 'value': 'application/json'},
      ],
      'body': json.dumps({'time': datetime.datetime.now().isoformat()})
    }
    self.send(response)


  def sendError(self, code=503):
    
    response = {
      'code': code, 
      'headers': [], 
      'body': ''
    }
    self.send(response)


  def send(self, response):

    self.send_response(response['code'])
    for header in response['headers']:
      self.send_header(header['name'], header['value'])
    self.end_headers()
    self.wfile.write(bytes(response['body'], 'utf-8'))


server = http.server.HTTPServer((ADDRESS, PORT), RequestHandler)
try:
  print('Listening at port %d' % PORT)
  server.serve_forever()
except KeyboardInterrupt:
  print('\nServer closing...\n')
finally:
  server.server_close()