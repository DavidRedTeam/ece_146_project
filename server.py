import socket
import time
message = "Hello client"

# server <-> router3
Fa0_1_ip = "192.168.5.2"
Fa0_1_mac = "12:AB:6A:DD:CC:10"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000

s.bind(("localhost", port))
# print("Socket binded to %s" %(port))

s.listen(2)
# print("socket is listening")


def deCapsulate(msg):
    # source_mac = msg[0:17]
    # destination_mac = msg[17:34]
    # source_ip = msg[34:45]
    # destination_ip = msg[45:56]
    # message = msg[56:]
    print("Received from Client")
    print("Destination MAC: ",  msg[0:17], " Source MAC: ", msg[17:34],
          " Source IP: ", msg[34:45], " Destination IP: ", msg[45:56],
          " Message: ", msg[56:])




while True:
    routerCon, addr = s.accept()
    if(routerCon != None):
        print("Router 3 connected ")
        break

while True:
    # ethernet_header = ""
    # ip_header = ""
    msg = routerCon.recv(1024).decode("utf-8")
    # message = input("\nEnter the text message to send: ")

    deCapsulate(msg)
    # dest_ip = input("Enter the IP of the clients \n(Only 192.168.1.2)")
    # add another if more clients
    # if(dest_ip == "192.168.1.2"):
    # swap the ip's source becomes destination and destination becomes source, server to client
    source_ip = Fa0_1_ip
    dest_ip = msg[34:45]
    ip_header = source_ip + dest_ip
    # print(ip_header)
    source_mac = Fa0_1_mac
    # dest_mac = router3_mac
    dest_mac = msg[17:34]
    ethernet_header = dest_mac + source_mac

    frame = ethernet_header + ip_header + message
    # print(packet)
    routerCon.sendall(bytes(frame, "utf-8"))
    #else:
     #   print("Wrong client IP inputted")
