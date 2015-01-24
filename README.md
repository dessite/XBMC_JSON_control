# XBMC_JSON_control
Simple app to control XBMC via JSON requests
The goal is to run this app on Raspberry PI with Raspbmc and control XBMC via push-buttons connected to GPIO
Currently it reads input from stdin however I plan to add support for Raspberry PI GPIO in the future, when I'll have some time to buy needed components and build steering board.

The app currently discovers XBMC instances with Zeroconf enabled, and then controls XBMC via simple JSON-RPC requests provided by XBMC JSON-RPC API
