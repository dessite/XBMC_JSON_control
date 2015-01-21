#!/usr/bin/python3

__author__ = 'Dessite'
__url__ = 'https://github.com/dessite/XBMC_JSON_control'
__email_ = 'fubu666@gmail.com'

import json

import requests

# Directions
_up = {"jsonrpc": "2.0", "method": "Input.up", "id": "1"}
_down = {"jsonrpc": "2.0", "method": "Input.down", "id": "1"}
_left = {"jsonrpc": "2.0", "method": "Input.left", "id": "1"}
_right = {"jsonrpc": "2.0", "method": "Input.right", "id": "1"}
_select = {"jsonrpc": "2.0", "method": "Input.select", "id": "1"}

# XBMC JSON-RPC API URL
_url = "http://192.168.1.105/jsonrpc"

print("Welcome to XBMC_JSON_CONTROL")
print("Enter u for up, d for down, l for left, r for right")
print("Enter s to select")
print("Enter q to quit")

while True:
    try:
        key = input()
    except:
        print("Something went wrong, exiting")
        break

    if key == 'u':
        try:
            request = requests.post(_url, data=json.dumps(_up))
        except:
            print("Somethings wrong, is Your XBMC running?")
    elif key == 'd':
        try:
            request = requests.post(_url, data=json.dumps(_down))
        except:
            print("Somethings wrong, is Your XBMC running?")
    elif key == 'l':
        try:
            request = requests.post(_url, data=json.dumps(_left))
        except:
            print("Somethings wrong, is Your XBMC running?")
    elif key == 'r':
        try:
            request = requests.post(_url, data=json.dumps(_right))
        except:
            print("Somethings wrong, is Your XBMC running?")
    elif key == 's':
        try:
            request = requests.post(_url, data=json.dumps(_select))
        except:
            print("Somethings wrong, is Your XBMC running?")
    elif key == 'q':
        print("Goodbye")
        break
    else:
        print("You've entered something else")
        print("Enter u for up, d for down, l for left, r for right")
        print("Enter s to select")
        print("Enter q to quit")