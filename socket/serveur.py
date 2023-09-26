#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
s.setsockopt(socket.SOL_IP, socket.SO_REUSEADDR, 1)
print('Serveur démarré sur le port : ', PORT)

conn, address = s.accept()


while 1:
    commande = input('($)')
    conn.send(commande.encode())
    data = conn.recv(2048).decode()
    print('data recu : ', data)
# print('Connecté à ', address)
# print(conn.recv(2048).decode())


# s.close()
