#!/usr/bin/python3

__author__ = 'Dessite'
__url__ = 'https://github.com/dessite/XBMC_JSON_control'
__email_ = 'fubu666@gmail.com'

import json
import time
import socket

import requests
from zeroconf import *



# listener class for XBMC
class XBMClistener(object):
    info = []

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, service_type, name):
        self.info.append(zeroconf.get_service_info(service_type, name))


# search for running XBMC instances
def scan_for_xbmc():
    zeroconf = Zeroconf()
    xbmc_listener = XBMClistener()
    ServiceBrowser(zeroconf, "_xbmc-jsonrpc._tcp.local.", xbmc_listener)
    time.sleep(6)
    zeroconf.close()
    return xbmc_listener.info


# Select XBMC instance from list, if only one found use it
def select_xbmc(xbmc_instances):
    if len(xbmc_instances) == 1:
        print("Found " + xbmc_instances[0].name + " at IP: " + socket.inet_ntoa(xbmc_instances[0].address))
        return socket.inet_ntoa(xbmc_instances[0].address)
    elif len(xbmc_instances) > 1:
        for index, item in enumerate(xbmc_instances):
            print("Found instance with ID: " + str(index) + " - Named " + item.name + " at IP: " + socket.inet_ntoa(
                item.address))
        choice = input("\nInsert ID of XBMC instance You want to Control")
        try:
            return socket.inet_ntoa(xbmc_instances[int(choice)].address)
        except IndexError:
            print("You've entered wrong ID, aborting...")
        except ValueError:
            print("You've entered wrong ID, aborting...")
    else:
        return None


# control XBMC instance
def control_xbmc(_ip):
    if _ip is not None:
        # XBMC JSON-RPC API URL
        _url = "http://" + _ip + "/jsonrpc"

        # Directions
        _up = {"jsonrpc": "2.0", "method": "Input.up", "id": "1"}
        _down = {"jsonrpc": "2.0", "method": "Input.down", "id": "1"}
        _left = {"jsonrpc": "2.0", "method": "Input.left", "id": "1"}
        _right = {"jsonrpc": "2.0", "method": "Input.right", "id": "1"}
        _select = {"jsonrpc": "2.0", "method": "Input.select", "id": "1"}
        _back = {"jsonrpc": "2.0", "method": "Input.back", "id": "1"}

        print("Enter u for up, d for down, l for left, r for right")
        print("Enter s to select")
        print("Enter q to quit")

        # Control loop
        while True:
            try:
                key = input()
            except:
                print("Something went wrong, exiting")
                break

            if key == 'u':
                try:
                    requests.post(_url, data=json.dumps(_up))
                except:
                    print("Somethings wrong, is Your XBMC running?")
            elif key == 'd':
                try:
                    requests.post(_url, data=json.dumps(_down))
                except:
                    print("Somethings wrong, is Your XBMC running?")
            elif key == 'l':
                try:
                    requests.post(_url, data=json.dumps(_left))
                except:
                    print("Somethings wrong, is Your XBMC running?")
            elif key == 'r':
                try:
                    requests.post(_url, data=json.dumps(_right))
                except:
                    print("Somethings wrong, is Your XBMC running?")
            elif key == 's':
                try:
                    requests.post(_url, data=json.dumps(_select))
                except:
                    print("Somethings wrong, is Your XBMC running?")
            elif key == 'b':
                try:
                    requests.post(_url, data=json.dumps(_back))
                except:
                    print("Somethings wrong, is Your XBMC running?")
            elif key == 'q':
                break
            else:
                print("You've entered something else")
                print("Enter u for up, d for down, l for left, r for right")
                print("Enter s to select")
                print("Enter q to quit")
    else:
        print("There are no XBMC instances, aborting...")


if __name__ == "__main__":
    print("Welcome to XBMC_JSON_CONTROL")
    print("Searching for XBMC instances, please wait")
    try:
        control_xbmc(select_xbmc(scan_for_xbmc()))
    finally:
        print("Goodbye")