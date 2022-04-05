import socket
import time

#router socket
router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.bind(("Localhost", 2000))

#socket for clients to connect to
router_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router_send.bind(("Localhost", 2001))

#router mac address
router_mac = "05:10:0A:CB:24:EF"

#server 
server  = ("Localhost", 8000)

#clients TODO: add more clients
client1_ip = "192.168.1.2"
client1_mac = "12:AB:6A:BA:DD:C6"


#Listen for clients, number for listen can be change for the amount of clients
router_send.listen(1)

client1 = None

while (client1 == None):
	client, address = router_send.accept()

	if (client1 == None):
		client1 = client
		print("Client 1 is online")

#simple arp table, keeps track of client IP addresses TODO: add more clients 
arp_table_socket = {client1_ip: client1}
#keeps track of client MAC addresses TODO: add more clients
arp_table_mac = {client1_mac: client1_mac}

#connect router to server
router.connect(server)


while True:
	received_message = router.recv(1024)
	received_message = received_message.decode("utf-8")
	
	#parsing the packet
	source_mac = received_message[0:17]
	destination_mac = received_message[17:34]
	source_ip = received_message[34:45]
	destination_ip = received_message[45:56]
	message = received_message[56:]

	print("The packed received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac = source_mac, destination_mac = destination_mac))

	print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))

	print("\n Message: " + message)

	ethernet_header = router_mac + arp_table_mac[destination_ip]

	IP_header = source_ip + destination_ip

	packet = ethernet_header + IP_header + message

	destination_socket = arp_table_socket[destination_ip]

	destination_socket.send(bytes(packet, "utf-8"))
	time.sleep(2)