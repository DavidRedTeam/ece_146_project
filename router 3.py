import socket
import time

#router 3 socket
router3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router3.bind(("Localhost", 2003))

router1 = ("Localhost", 2001)
router2 = ("Localhost", 2002)

#router info
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

router3_ip = "192.168.1.4"
router3_mac = "05:10:0A:DF:5A:4A"

#server info
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:C10"

#connect to server
port = 8000
server = (("localhost", port))

#Listen for router1 and router2 connection
router3.listen(2)

router1 = None
router2 = None

while (router1 == None or router2 == None or server == None):
    router, address = router3.accept()
    
    if(router1 == None):
        router1 = router
        print("Router 1 is online")
    
    elif(router2 == None):
        router2 = router
        print("Router 2 is online")  
  
arp_table_socket = {router1_ip: router1, router2_ip: router2, server_ip: server}
arp_table_mac = {router1_ip: router1_mac, router2_ip: router2_mac, server_ip: server_mac}

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

	print("The packet received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(source_mac = source_mac, destination_mac = destination_mac))

	print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip, destination_ip=destination_ip))

	print("\n Message: " + message)

	ethernet_header = router_mac + arp_table_mac[destination_ip]

	IP_header = source_ip + destination_ip

	packet = ethernet_header + IP_header + message

	destination_socket = arp_table_socket[destination_ip]

	destination_socket.send(bytes(packet, "utf-8"))
	time.sleep(2)
