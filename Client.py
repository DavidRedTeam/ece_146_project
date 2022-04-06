#Client that will connect to server through routers.
import socket
import time
#This clients mac and ip static.
client_ip = "192.168.1.2"
client_mac = "12:AB:6A:BA:DD:C6"

#Identifying the router we want to connect to. *Note that the socket will act as the ip since we are
#defining the client, routers, and server on the same computer.
router1 = ("LocalHost", 2001)

#make the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the router
client.connect(router1) #not created yet but waiting to merge code.

#This will handle the message we send and receive.
print(("Please enter a message to send"))
connected = True
while connected:
    message = input()
    if message.find("quit") != -1: connected = False
    client.sendall(bytes(message, "utf-8"))
    recv_message = client.recv(1024).decode("utf-8")
    print(recv_message)