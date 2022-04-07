# Client that will connect to server through routers.
import socket
import time

# This clients mac and ip static.
client_ip = "192.168.1.2"
client_mac = "12:AB:6A:BA:DD:C6"


#Identifying the router we want to connect to. *Note that the socket will act as the ip since we are
#defining the client, routers, and server on the same computer.
router1 = ("LocalHost", 2001)

#server info
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:CC:10"

# Identifying the router we want to connect to. *Note that the socket will act as the ip since we are
# defining the client, routers, and server on the same computer.
router1 = ("LocalHost", 2000)


# make the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the router dummy router
client.connect(router1)

source_mac = client_mac
dest_mac = server_mac

source_ip = client_ip
dest_ip = server_ip

# This will handle the message we send and receive.
print("Please enter a message to send")

# This is the frame, and packet that will be sent across the routers and network.


outgoing_frame = source_mac + dest_mac + source_ip + dest_ip

def deCapsulate(msg):
    # source_mac = msg[0:17]
    # destination_mac = msg[17:34]
    # source_ip = msg[34:45]
    # destination_ip = msg[45:56]
    # message = msg[56:]
    print("Source MAC: ",  msg[0:17]," Destination MAC: ", msg[17:34],
          " Source IP: ", msg[34:45], " Destination IP: ", msg[45:56],
          " Message: ", msg[56:])


connected = True
while connected:
    message = input("client2server>")

    if message.find("quit") != -1: connected = False
    outgoing_frame = outgoing_frame + message
    client.send(bytes(outgoing_frame, "utf-8"))
    outgoing_frame = outgoing_frame[0:56]
    recv_message = client.recv(1024).decode("utf-8")

    deCapsulate(recv_message)





