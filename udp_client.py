from http import client
host = "localhost"
port = 9999
address = (host,port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("Enter a word : ")
    
    if data == "exit":
         data = data.encode('utf8')
         client.sendto(data , address)
        
         print("Disconnection")
         break
    
    data = data.encode('utf8')
    client.sendto(data , address)
    
    data , address = client.recvfrom(1024)
    data = data.decode('utf8')
    print(f"Server: {data}")
    
client.close()


