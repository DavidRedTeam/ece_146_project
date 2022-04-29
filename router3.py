import socket
import time


router2 = ("Localhost", 2003)
router1 = ("Localhost", 2004)

router32router2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router32router2.bind(router2)
# router32router2.setblocking(False)

router32router1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router32router1.bind(router1)
# router32router1.setblocking(False)

server = ("LocalHost", 8000)
toServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
toServer.connect(server)

# router info
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

router3_ip = "192.168.1.4"
router3_mac = "05:10:0A:DF:5A:4A"

# server info
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:C10"

# Interfaces and their IP's (Serial does not have mac addresses)
# router3 <-> router1
#serial0_1_0 = "192.168.3.1"

# router3 <-> router2
gigEth0_1_0_ip = "192.168.4.2"
gigEth0_1_0_mac = "05:10:0A:BB:A1:C8"

# router3 <-> Server
gigEth0_0_1_ip = "192.168.5.1"
gigEth0_0_1_mac = "05:10:0A:DF:5A:4A"



def bandwidth_scaling(bandwidth):
    bandwidth_scaled = (10000000 / bandwidth) * 256
    return bandwidth_scaled


def delay_scaling(delay):
    delay_scaled = delay * 256
    return delay_scaled


# Listen for router1 and router2 connection
router32router1.listen(1)
router32router2.listen(1)

fromrouter1, address = router32router1.accept()
fromrouter2, address = router32router2.accept()
# framePath2, address2 = router32router1.accept()

if fromrouter1:
    print("Router 1 connected")

if fromrouter2:
    print("Router 2 connected")


# elif(router2 == None):
# router2 = router2Router
# print("Router 2 is online")
# arp_table_socket = {router1_ip: router1, router2_ip: router2, server_ip: server}
# arp_table_mac = {router1_ip: router1_mac, router2_ip: router2_mac, server_ip: server_mac}

# router2Router.connect(server)
router3torouter1_b = 2000 #router1 to router3 bandwidth
router3torouter1_d = 600   #router1 to router3 delay

router3torouter2_b = 5000 #router3 to router2 bandwidth
router3torouter2_d = 600 #router3 to router2 delay

router2torouter1_b = 5000     #router2 to router1 bandwidth
router2torouter1_d = 500	  #router2 to router1 delay

def calc_metric(bandwidth, delay):
	return 256 * ((pow(10, 7) / bandwidth) + (delay / 10))

def create_route(destination, next_hop, hop_count, metric):
	return routes(destination, next_hop, hop_count, metric)

class routes:
	def __init__(self, destination, next_hop, hop_count, metric):
		self.destination = destination
		self.next_hop = next_hop
		self.hop_count = hop_count
		self.metric = metric

	def getDestionation(self):
		return self.destination

	def getnext_hop(self):
		return self.next_hop

	def gethop_count(self):
		return self.hop_count
	def getmetric(self):
		return self.metric

route3to1 = 1
route3to2 = 2
router3to1_m = calc_metric(router3torouter1_b, router3torouter1_d)
router3to2_m = calc_metric(router3torouter2_b, router3torouter2_d)
router2to1_m = calc_metric(router2torouter1_b, router2torouter1_d)
router_table = []
router_table.append(create_route(server_ip, router1, route3to1, router3to1_m))
router_table.append(create_route(server_ip, router2, route3to2, router3to2_m + router2to1_m))

fromrouter1.settimeout(1)
fromrouter2.settimeout(1)
message1 = " "
message2 = " "
while True:
    try:
        time.sleep(router3torouter1_d/10000)
        message1 = fromrouter1.recv(1024).decode("utf-8")

        print("sending to server")
        messageEthernet = "12:AB:6A:DD:CC:10" + gigEth0_0_1_mac + message1
        print("Ethernet: ", messageEthernet)
        toServer.sendall(bytes(messageEthernet, "utf-8"))
        print("receiving from server")
        time.sleep(router3torouter1_d/10000)
        reply = toServer.recv(1024).decode("utf-8")

        messageSerial = reply[34:45] + reply[45:56] + reply[56:]
        print("Serial Reply: ", messageSerial)
        if router_table[0].getmetric() < router_table[1].getmetric():
            print("sending to router1")
            time.sleep(router3torouter1_d/10000)
            fromrouter1.sendall(bytes(messageSerial, "utf-8"))
            fromrouter1.setblocking(1)

    except socket.timeout:
        print("router 1 timeout")

    try:
        time.sleep(router3torouter2_d/10000)
        message2 = fromrouter2.recv(1024).decode("utf-8")
        messageEthernet = "12:AB:6A:DD:CC:10" + gigEth0_0_1_mac + message2[34:45] + message2[45:56] + message2[56:]
        print("Ethernet: ", messageEthernet)
        toServer.sendall(bytes(messageEthernet, "utf-8"))
        time.sleep(router3torouter2_d/10000)
        reply = toServer.recv(1024).decode("utf-8")
        messageEthernet = "05:10:0A:AA:FF:54" + gigEth0_1_0_mac + reply[34:45] + reply[45:56] + reply[56:]
        print("to router 2: " , messageEthernet)
        if router_table[1].getmetric() < router_table[0].getmetric():
            print("sending to router2")
            time.sleep(router3torouter2_d/10000)
            fromrouter2.sendall(bytes(messageEthernet, "utf-8"))
            fromrouter2.setblocking(1)
    except socket.timeout:
        print("router 2 timeout")

# parsing the packet
# source_mac = received_message[0:17]
# destination_mac = received_message[17:34]
# source_ip = received_message[34:45]
# destination_ip = received_message[45:56]
# message = received_message[56:]
# if message1.find("." or ":") == -1:
# from1.setblocking(1)
# toServer.sendall(bytes(message2, "utf-8"))
# reply = toServer.recv(1024).decode("utf-8")
# from2.sendall(bytes(reply, "utf-8"))
# elif message2.find("." or ":") == -1:
# from2.setblocking(1)
# toServer.sendall(bytes(message1, "utf-8"))
# reply = toServer.recv(1024).decode("utf-8")
# from1.sendall(bytes(reply, "utf-8"))

# print("The packet received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac = source_mac, destination_mac = destination_mac))

# print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))

# print("\n Message: " + message)

# ethernet_header = router_mac + arp_table_mac[destination_ip]

# IP_header = source_ip + destination_ip

# packet = ethernet_header + IP_header + message

# destination_socket = arp_table_socket[destination_ip]

# destination_socket.send(bytes(packet, "utf-8"))
# time.sleep(2)
