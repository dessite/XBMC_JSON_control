__author__ = 'fuf'
import requests
import json

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
        print("cos innego")