import socket
import threading

ip = "0.0.0.0"
port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind((ip,port))

#server.listen(5)

print ("[*] Welcome to server,you now connected to %s:%d" % (ip,port))

def handle_client(client_socket):
    request = client_socket.recv(1024)

    print ("Recieved request %s"%request)

    #send the packet back to client
    client_socket.sendto("ACK!..",("vampire",9999))

    client_socket.close()

while True:
    client,addr = server.recvfrom(1024)

    print ("[*] Accepted connection from %s:%d" % (addr[0],addr[1]))

    #spin up our client thread to handle incomming data 
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
