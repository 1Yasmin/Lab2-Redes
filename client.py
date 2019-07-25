#Cristian Perez C16011 Yasmin Chavez C16101
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("msg to send: ")
    s.sendall(msg.encode())
    data = s.recv(1024).decode()

print('Received', repr(data))
