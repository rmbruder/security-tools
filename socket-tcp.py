import socket
## File name cannot be socket.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sans.org', 80))  # host and port in a () tuple

s.send(b'GET / HTTP/1.1\r\nHost: www.sans.org\r\n\r\n')
data=s.recv(1024)
s.close()
print(data)


