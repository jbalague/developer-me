## Anatomy of a REST API Server

While learning some HTTP and Python...

### Minimal server (GET)

Let's start with a simple http server
``` python
import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    self.wfile.write(bytes('<h1>Bello bol!</h1>', 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()
```

Python 101
- Standard Library modules
- Classes


Introducing curl...
``` shell
curl 127.0.0.1:8787
```

Browsers not working?

- Safari
```
Safari can’t open the page
Safari can’t open the page “‎127.0.0.1:8787” because the server unexpectedly dropped the connection. This sometimes occurs when the server is busy. Wait for a few minutes, and then try again.
```

- Chrome
```
This page isn't working
127.0.0.1 sent an invalid response.
ERR_INVALID_HTTP_RESPONSE
```

- Firefox 
```
<h1>Bello bol!</h1>
```

Let's see what's going on...
``` shell
curl -v 127.0.0.1:8787
```

``` shell
$ curl -v 127.0.0.1:8787
* Rebuilt URL to: 127.0.0.1:8787/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8787 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8787
> User-Agent: curl/7.54.0
> Accept: */*
>
* Connection #0 to host 127.0.0.1 left intact
<h1>Bello bol!</h1>$
```

HTTP 101
- Method - Purpose
- Path - What
- Headers - Metadata
- Body - Data

A sligthly better HTML response
``` python
import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

    self.wfile.write(bytes('<h1>Bello bol!</h1>', 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()
```

``` shell
$ curl -v 127.0.0.1:8787
* Rebuilt URL to: 127.0.0.1:8787/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8787 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8787
> User-Agent: curl/7.54.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: BaseHTTP/0.6 Python/3.6.4
< Date: Mon, 26 Feb 2018 09:11:23 GMT
< Content-type: text/html
<
* Closing connection 0
<h1>Bello bol!</h1>$
```

And all browsers working now!

Adding more standard/custom headers...

``` python
import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.send_header('MyHeader', 'developer-me')
    self.end_headers()

    self.wfile.write(bytes('<h1>Bello bol!</h1>', 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()
```

Inspecting received headers

``` python
import http.server

class RequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

    response = '<h1>Bello bol!</h1>'
    for header in self.headers:
      response = response + '<br>' + header + ': ' + self.headers[header]
    
    self.wfile.write(bytes(response, 'utf-8'))


server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()
```

Python 102
- Iteration

Exploring unknown paths

``` python
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
```

Python 103
- Branching

What time is it? + JSON

``` python
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
```

Curling headers

``` shell
curl -v -H 'Accept: application/json' 127.0.0.1:8787/api/time
```

Python 104
- datetime
- json

There are other methods

``` python
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
``` 

Curling methods and data

``` shell
curl -v -H 'Content-type: application/json' -d '{"text": "lalala"}' 127.0.0.1:87
```

``` shell
$ curl -v -H 'Content-type: application/json' -d '{"text": "lalala"}' 127.0.0.1:87
87/api/log
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8787 (#0)
> POST /api/log HTTP/1.1
> Host: 127.0.0.1:8787
> User-Agent: curl/7.54.0
> Accept: */*
> Content-type: application/json
> Content-Length: 18
>
* upload completely sent off: 18 out of 18 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: BaseHTTP/0.6 Python/3.6.4
< Date: Mon, 26 Feb 2018 14:23:56 GMT
< Content-type: application/json
<
* Closing connection 0
{"status": "OK", "message": "lalala"}$
``` 

``` shell
curl -v -H 'Content-type: application/json' -d -X POST '{"text": "lalala"}' 127.0.0.1:87
```

Query strings and parameters I (GET)

``` python
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
```

Query strings and parameters II (POST)

``` python
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

    url = urlparse(self.path)
    path = url.path
    query = parse_qs(url.query)

    dataLength = int(self.headers['Content-Length'])
    rawData = self.rfile.read(dataLength)

    if url.path == '/api/log':
      if self.headers['Content-type'] == 'application/json':
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
    elif url.path == '/api/best':
      name = ''
      if self.headers['Content-type'] == 'application/json':
        name = json.loads(rawdata)
      
      elif self.headers['Content-type'] == 'application/x-www-form-urlencoded':
        params = parse_qs(rawData)
        if b'name' in params:
          name = params[b'name'][0].decode('utf-8')

      elif 'name' in query:
          name = query['name'][0]
      
      if name != '':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = name + ' is the best minion!'
      
      else:
        self.send_response(404)
        self.end_headers()
        response = ''        

    print(response)
    self.wfile.write(bytes(response, 'utf-8'))

server = http.server.HTTPServer(('127.0.0.1', 8787), RequestHandler)
server.serve_forever()
```

Time to refactor

``` python
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
``` 



----
# TO DO
- Cookies
- Client