from http import server
import socket

host = "localhost"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host,port))

while True:
    data ,address = server.recvfrom(1024)
    data = data.decode('utf-8')
    
    if data == "exit" : 
         print("Client disconnected")
         break
    
    print(f"Client : {data}") 
    
    data = data.upper()
    data = data.encode('utf-8')
    server.sendto(data,address)

server.close()
