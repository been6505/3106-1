from pydoc import cli
import socket

host = "localhost"
port = 9999

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

data = input("Enter : ")
client.send(bytes(data.encode('utf-8')))
buffer = client.recv(1024)
buffer = buffer.decode('utf-8')
print(f"Server : {buffer}")
