import socket
import time
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:C10"

router3_mac = "05:10:0A:DF:5A:4A"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("LocalHost", 2008))
#print("Socket binded to %s" %(port))

server.listen(1)
print("socket is listening")

while True:
    routerCon, address = server.accept()
    if(routerCon != None):
        print(routerCon)
        break

while True:
    ethernet_header = ""
    ip_header = ""

    message = input("\nEnter the text message to send: ")

    dest_ip = input("Enter the IP of the clients \n(Only 192.168.1.2)")
    #add another if more clients
    if(dest_ip == "192.168.1.2"):
        source_ip = server_ip
        ip_header = ip_header + source_ip + dest_ip

        source_mac = server_mac
        dest_mac = router3_mac

        ethernet_header = ethernet_header + source_mac + dest_mac

        packet = ethernet_header + ip_header + message

        routerCon.send(packet.encode("utf-8"))
    else:
        print("Wrong client IP inputted")