#!/usr/bin/env python
# -- coding: utf-8 --
#Cristian Perez C16011 Yasmin Chavez C16101
import socket
import pickle
import struct
from bitarray import bitarray

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # find the length of the packet
            buf = b''
            while len(buf) < 4:
                buf += conn.recv(4 - len(buf))
            length = struct.unpack('>I', buf)[0]
            print(length)
            # recieve the data
            data = conn.recv(length)
            if not data:
                break
            # return the data to bitarray
            print(data)
            msg = pickle.loads(data)
            print("message from: ", addr, msg)

