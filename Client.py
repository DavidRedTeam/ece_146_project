# Client that will connect to server through routers.
# Assume arp table and routing tables are set up on routers and host and server.!!!!!!!!!
import socket
import time

# This clients mac and ip static. This is the only interface
# Fa0/0's ip and mac.
Fa0_0_ip = "192.168.1.2"
Fa0_0_mac = "12:AB:6A:BA:DD:C6"


#Identifying the router we want to connect to. *Note that the socket will act as the ip since we are
#defining the client, routers, and server on the same computer.
#Gateway == Router1.
gateWay = ("LocalHost", 2001)
gateWay_mac = "05:10:0A:CB:24:EF"

#server info
server_ip = "192.168.5.2"

# Identifying the router we want to connect to. *Note that the socket will act as the ip since we are
# defining the client, routers, and server on the same computer.
#router1 = ("LocalHost", 2000)


# make the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the router dummy router
client.connect(gateWay)

source_mac = Fa0_0_mac
dest_mac = gateWay_mac

source_ip = Fa0_0_ip
dest_ip = server_ip

# This will handle the message we send and receive.
print("Please enter a message to send")

# This is the frame, and packet that will be sent across the routers and network.

outgoing_frame = dest_mac + source_mac + source_ip + dest_ip

def deCapsulate(msg):
    # source_mac = msg[0:17]
    # destination_mac = msg[17:34]
    # source_ip = msg[34:45]
    # destination_ip = msg[45:56]
    # message = msg[56:]
    print("Received from Server")
    print("Destination MAC: ",  msg[0:17], " Source MAC: ", msg[17:34],
          " Source IP: ", msg[34:45], " Destination IP: ", msg[45:56],
          " Message: ", msg[56:])


connected = True
while connected:
    message = input("client2server>")


    outgoing_frame = outgoing_frame + message
    client.sendall(bytes(outgoing_frame, "utf-8"))
    if message.find("quit") != -1: client.close()
    outgoing_frame = outgoing_frame[0:56]
    recv_message = client.recv(1024).decode("utf-8")

    deCapsulate(recv_message)





