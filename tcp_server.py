import socket

host = "localhost"
port = 9999


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

while True:
    client,address = server.accept()
    
    print(f"Connect to server : {address[0]} : {address[1]}")
    
    
    data = client.recv(1024)
    data = data.decode('utf-8')
    print(data)
    
    data = data.upper()
    client.send(bytes(data,'utf-8'))
    
    client.close()
    
