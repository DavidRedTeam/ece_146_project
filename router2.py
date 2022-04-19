# has connection from router1 needs to connect to router3

import socket
import time

router22router1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router22router1.bind(("Localhost", 2002))

router3 = ("LocalHost", 2003)
router22router3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router22router3.connect(router3)

# router mac address
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

router3_ip = "192.168.1.4"
router3_mac = "05:10:0A:DF:5A:4A"

# connect to router3
# router3 = ("Localhost", 2003)

# Listen for router1 connection

router22router1.listen(1)

# router1 = None




# while (router1 == None):
router2Router, address = router22router1.accept()

# if (router1 == None):
# router1 = router
if router2Router:
	print("Router 1 is connected")


# TODO: FIX ARP TABLE TO INCLUDE THE OTHER ROUTERS
# arp_table_socket = {router1_ip: router1}
# arp_table_mac = {router1_ip: router1_mac}

while True:
	message = router2Router.recv(1024).decode("utf-8")
	print(message)
	# parsing the packet
	#  source_mac = received_message[0:17]
	# destination_mac = received_message[17:34]
	# source_ip = received_message[34:45]
	# destination_ip = received_message[45:56]
	# message = received_message[56:]

	router22router3.sendall(bytes(message, "utf-8"))

	# print("The packet received:\n Source MAC address: {source_mac},
	# Destination MAC address: {destination_mac}".format(source_mac = source_mac, destination_mac = destination_mac))

	# print("\nSource IP address: {source_ip},
	# Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))

	# print("\n Message: " + message)

	# ethernet_header = router_mac + arp_table_mac[destination_ip]

	# IP_header = source_ip + destination_ip

	# packet = ethernet_header + IP_header + message

	# destination_socket = arp_table_socket[destination_ip]

	# destination_socket.send(bytes(packet, "utf-8"))
	# time.sleep(2)

	reply = router22router3.recv(1024).decode("utf-8")
	print(reply[56:0])
	router2Router.sendall(bytes(reply, "utf-8"))
