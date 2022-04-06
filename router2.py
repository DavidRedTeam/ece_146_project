#has connection from router1 needs to connect to router3

import socket
import time

router2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router2.bind(("Localhost", 2002))


#router mac address
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

router3_ip = "192.168.1.3"
router3_mac = "05:10:0A:DF:5A:4A"

#connect to router3
router3 = ("Localhost", 2003)

#Listen for router1 connection

router2.listen(1)

router1 = None

while (router1 == None):
	router, address = router2.accept()

	if (router1 == None):
		router1 = router
		print("Router 1 is connected")

arp_table_socket = {router1_ip: router1}
arp_table_mac = {router1_ip: router1_mac}

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