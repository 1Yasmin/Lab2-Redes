#!/usr/bin/env python
# -- coding: utf-8 --
#Cristian Perez C16011 Yasmin Chavez C16101
import socket
import pickle

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1204)
        print(data)
        msg = pickle.loads(data)
        print("message from: ", addr, msg.tobytes().decode('ascii'))
        if not data:
            break

