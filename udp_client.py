from http import client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Start Server".encode('utf8'),("localhost",9999))
print(client.recvfrom(1024)[0].decode('utf8'))



