import socket
import threading

target_host = "vampire"
target_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("hello")
response = client.recv(4096)

print (response)