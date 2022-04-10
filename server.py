import socket
import time
message = "Hello client"
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:CC:10"

router3_mac = "05:10:0A:CB:24:EF"
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
    print("Source MAC: ",  msg[0:17]," Destination MAC: ", msg[17:34],
          " Source IP: ", msg[34:45], " Destination IP: ", msg[45:56],
          " Message: ", msg[56:])




while True:
    routerCon, addr = s.accept()
    if(routerCon != None):
        print("Router 1 connected ")
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
    source_ip = msg[45:56]
    dest_ip = msg[34:45]
    ip_header = source_ip + dest_ip
    # print(ip_header)
    source_mac = server_mac
    # dest_mac = router3_mac
    dest_mac = msg[0:17]
    ethernet_header = source_mac + dest_mac

    packet = ethernet_header + ip_header + message
    # print(packet)
    routerCon.sendall(bytes(packet, "utf-8"))
    #else:
     #   print("Wrong client IP inputted")
