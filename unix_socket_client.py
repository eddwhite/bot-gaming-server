#!/bin/python3
import socket
import os, os.path

socket_loc = "/home/edd/Workspace/unix_socket"

print("Connecting...")
if os.path.exists(socket_loc):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(socket_loc)

    print("Ready!")
    while True:
        in_str = input("> ")
        client.send(in_str.encode())


client.close()