import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',9999))

server.listen()

while True:
    client,address = server.accept()
    
    print(f"Connect to server : {address}")
    
    print(client.recv(1024).decode('utf-8'))
    client.send("Start connection to server".encode('utf-8'))
    
    print(client.recv(1024).decode('utf-8'))
    client.send("End connection".encode('utf-8'))
    
    client.close()
    
    