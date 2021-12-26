#!/usr/bin/python3

import socket

target_host = "127.0.0.1"
target_port = 9700

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()