from http import server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost",9999))

message,address = server.recvfrom(1024)
print(message.decode('utf-8'))
server.sendto("Start connection".encode('utf-8'),address)

