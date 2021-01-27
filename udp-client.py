import socket

target_host = "vampire"
target_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(b"Hello server",(target_host,target_port))

data,addr = client.recvfrom(1024)

print(data)