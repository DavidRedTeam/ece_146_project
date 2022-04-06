#Connects to client router2 and router3

import socket
import time

#router socket
router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.bind(("Localhost", 2000))

#socket for clients to connect to
router_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router_send.bind(("Localhost", 2001))

#router mac address
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

#connect to routers
router2 = ("Localhost", 2002)
router3 = ("Localhost", 2003)

#clients TODO: add more clients
client1_ip = "192.168.1.2"
client1_mac = "12:AB:6A:BA:DD:C6"

router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

router3_ip = "192.168.1.3"
router3_mac = "05:10:0A:DF:5A:4A"

#Listen for clients, number for listen can be change for the amount of clients
router_send.listen(1)

client1 = None

while (client1 == None or router2 == None or router3 == None):
	client, address = router_send.accept()

	if (client1 == None):
		client1 = client
		print("Client 1 is online")
	elif (router2 == None):
		router2 = client
		print("Router 2 is connected")
	else:
		router3 = client
		print("Router3 is connected")

#simple arp table, keeps track of client IP addresses TODO: add more clients 
arp_table_socket = {client1_ip: client1, router2_ip: router2, router3_ip: router3}
#keeps track of client MAC addresses TODO: add more clients
arp_table_mac = {client1_ip: client1_mac, router2_ip: router2_mac, router3_ip: router3_mac}

router.connect(router2)
#router.connect(router3)


while True:
	received_message = router.recv(1024)
	received_message = received_message.decode("utf-8")
	
	#parsing the packet
	source_mac = received_message[0:15]
	print(source_mac)
	destination_mac = received_message[15:32]
	print(destination_mac)
	source_ip = received_message[32:43]
	print(source_ip)
	destination_ip = received_message[43:54]
	print(destination_ip)
	message = received_message[54:]
	print(message)

	print("The packet received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac = source_mac, destination_mac = destination_mac))

	print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))

	print("\n Message: " + message)

	ethernet_header = router_mac + arp_table_mac[destination_ip]

	IP_header = source_ip + destination_ip

	packet = ethernet_header + IP_header + message

	destination_socket = arp_table_socket[destination_ip]

	destination_socket.send(bytes(packet, "utf-8"))
	time.sleep(2)