import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.send("Hello World".encode())

data = s.recv(1024)
data = data.decode()

print(data)
s.close()