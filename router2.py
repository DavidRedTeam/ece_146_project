import socket
import time

#hop metric
hop_count_router1 = 2
hop_count_router3 = 1

router1 = ("LocalHost", 2002)

#if(hop_count_router1 < hop_count_router3):
router22router1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router22router1.bind(router1)

#if(hop_count_router1 > hop_count_router3):
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

server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:C10"

# connect to router3
# router3 = ("Localhost", 2003)
def bandwidth_scaling(bandwidth):
	bandwidth_scaled = (10000000/bandwidth) * 256
	return bandwidth_scaled


def delay_scaling(delay):
	delay_scaled = delay * 256
	return delay_scaled
# Listen for router1 connection

router22router1.listen(1)

# router1 = None

# while (router1 == None):
router2Router, address = router22router1.accept()

# if (router1 == None):
# router1 = router
if router2Router:
	print("Router 1 is connected")

def create_route(destination, next_hop, hop_count):
    return routes(destination, next_hop, hop_count)


class routes:
    def __init__(self, destination, next_hop, hop_count):
        self.destination = destination
        self.next_hop = next_hop
        self.hop_count = hop_count

    def getDestionation(self):
        return self.destination

    def getnext_hop(self):
        return self.next_hop

    def gethop_count(self):
        return self.hop_count

route2to1 = 1
route2to3 = 1

router_table = []
router_table.append(create_route(server_ip, router1, route2to1))
router_table.append(create_route(server_ip, router3, route2to3))
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
