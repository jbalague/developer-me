import urllib.request
import time

SERVER = 'http://127.0.0.1:8787'
URL = SERVER + '/time.text'

try:
  while True:  
    request = urllib.request.urlopen(URL)
    print(request.read().decode())
    time.sleep(0.99)

except KeyboardInterrupt:
  print('bye')
