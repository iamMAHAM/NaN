#!/usr/bin/env python3

import socket
HOST = '127.0.0.1'
PORT = 3000

s = socket.socket()

s.bind((HOST, PORT))
