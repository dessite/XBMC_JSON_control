__author__ = 'Dessite'
__url__ = 'https://github.com/dessite/XBMC_JSON_control'
__email_ = 'fubu666@gmail.com'

import json

import requests


left = {"jsonrpc": "2.0", "method": "Input.left", "id": "1"}
url = "http://192.168.1.105/jsonrpc"

while True:
    key = input()
    if key == 'l':
        request = requests.post(url, data=json.dumps(left))
        print(request.json())
    elif key == 'b':
        break
    else:
        print("something else")