# Connects to client router2 and router3

import socket
import time

# router socket
router2 = ("LocalHost", 2002)
router12router2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# router12router2.bind(("Localhost", 2000))
router12router2.connect(router2)

# socket for clients to connect to
router2client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router2client.bind(("Localhost", 2001))
router2client.listen(1)

router3 = ("LocalHost", 2004)
router12router3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router12router3.connect(router3)

# router mac address
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

# connect to routers
# router2 = ("Localhost", 2002)
# router3 = ("Localhost", 2003)
# server = ("localhost", 8000)

# clients TODO: add more clients
# client1_ip = "192.168.1.2"
# client1_mac = "12:AB:6A:BA:DD:C6"

# router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

# router3_ip = "192.168.1.4"
router3_mac = "05:10:0A:DF:5A:4A"

# Listen for clients, number for listen can be change for the amount of clients


# TODO: FIX ARP TABLE TO INCLUDE THE OTHER ROUTERS
# simple arp table, keeps track of client IP addresses TODO: add more clients
# arp_table_socket = {client1_ip: client1, router2_ip: router2, router3_ip: router3}
# keeps track of client MAC addresses TODO: add more clients
# arp_table_mac = {client1_ip: client1_mac, router2_ip: router2_mac, router3_ip: router3_mac}

def create_route(destination, next_hop, hop_count):
	return routes(destination, next_hop, hop_count)

class routes:
	def __init__(self, destination, next_hop, hop_count):
		self.destination = Destination
		self.next_hop = next_hop
		self.hop_count = hop_count

	def getDestionation(self):
		return self.destination

	def getnext_hop(self):
		return self.next_hop

	def gethop_count(self):
		return self.hop_count

server_ip = "192.168.0.1"
# client1 = None
#router_table = {Destination: [next_hop_port, hop count]}

route1to2 = 2
route1to3 = 1
clientRouter, address = router2client.accept()
router_table = []
router_table.append(create_route(server_ip, router3, route1to3))
router_table.append(create_route(server_ip, router2, router1to2))

if clientRouter:
	print("Client Connected")

# while (client1 == None or router2 == None or router3 == None):
while True:
	message = clientRouter.recv(1024).decode("utf-8")

	# if (client1 == None):
	client1 = clientRouter
	#print("Client 1 is online")

	# router.connect(router2)
	# router.connect(router3)

	# while True:
	print("Here")
	if route1to2 > route1to3:
		router12router3.sendall(bytes(message,"utf-8"))
		reply = router12router3.recv(1024).decode("utf-8")
	else:
		router12router2.sendall(bytes(message, "utf-8"))
		reply = router12router2.recv(1024).decode("utf-8")

	print("Here")
	# received_message = received_message.decode("utf-8")

	# parsing the packet
	# source_mac = received_message[0:17]
	# destination_mac = received_message[17:34]
	# source_ip = received_message[34:45]
	# destination_ip = received_message[45:56]
	# message = received_message[56:]

	# print("The packet received:\n Source MAC address: {source_mac},
	# Destination MAC address: {destination_mac}".format(source_mac = source_mac, destination_mac = destination_mac))

	# print("\nSource IP address: {source_ip},
	# Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))

	# print("\n Message: " + message)

	# ethernet_header = router1_mac + arp_table_mac[destination_ip]

	# IP_header = source_ip + destination_ip

	# packet = ethernet_header + IP_header + message
	# destination_socket = arp_table_socket[destination_ip]

	# destination_socket.send(bytes(packet, "utf-8"))
	# time.sleep(2)

	clientRouter.sendall(bytes(reply, "utf-8"))





