import socket
import time
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:C10"

router3_mac = "12:AB:6A:BA:DD:C9"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000

s.bind(("localhost", port))
#print("Socket binded to %s" %(port))

s.listen(2)
#print("socket is listening")

while True:
    routerCon, addr = s.accept()
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

        routerCon.send(bytes(packet, "utf-8"))
    else:
        print("Wrong client IP inputted")
