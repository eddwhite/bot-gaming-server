#!/bin/python3
import socket
import os, os.path

socket_loc = "/home/edd/Workspace/unix_socket"

if os.path.exists(socket_loc):
    os.remove(socket_loc)

print("Opening socket")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(socket_loc)

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print(datagram)


server.close()
os.remove(socket_loc)