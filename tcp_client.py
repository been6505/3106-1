from pydoc import cli
import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",9999))

client.send("Start server".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

client.send("Stop server".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

