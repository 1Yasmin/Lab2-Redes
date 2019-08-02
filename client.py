#!/usr/bin/env python
# -- coding: utf-8 --
#Cristian Perez C16011 Yasmin Chavez C16101
import socket
import pickle
from utils import *

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("msg to send: ")
    msg_bitarray = to_bitarray(msg)
    print(msg_bitarray)
    #msg_ruido = random_error(msg_bitarray)
    s.sendall(pickle.dumps(msg_bitarray))





