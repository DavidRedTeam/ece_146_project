import socket
import time

# router 3 socket
router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.bind(("LocalHost", 2004))

router_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router_send.bind(("LocalHost", 2005))

#router1 = ("Localhost", 2001)
#router2 = ("Localhost", 2002)

# router info
router1_ip = "192.168.1.1"
router1_mac = "05:10:0A:CB:24:EF"

router2_ip = "192.168.1.3"
router2_mac = "05:10:0A:DC:35:AF"

router3_ip = "192.168.1.3"
router3_mac = "05:10:0A:DF:5A:4A"

# server info
server_ip = "192.168.0.1"
server_mac = "12:AB:6A:DD:C10"

# connect to server
server = ("LocalHost", 2008)

# Listen for router1 and router2 connection
router_send.listen(2)

#router1 = None
router2 = None
server1 = None

while (router2 == None or server1 == None):
    router_recv, address = router_send.accept()

    '''if (router1 == None):
        router1 = router
        print("Router 1 is online")
    '''
    if(router2 == None):
        router2 = router_recv
        print("Router 2 is online")
    if(server1 == None):
        server1 = router_recv
        print("Server is online")

#arp_table_socket = {router1_ip: router1, router2_ip: router2, server_ip: server}
#arp_table_mac = {router1_ip: router1_mac, router2_ip: router2_mac, server_ip: server_mac}

router.connect(server)

while True:
    received_message = router_recv.recv(1024)
    received_message = received_message.decode("utf-8")

    # parsing the packet
    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]
    source_ip = received_message[34:45]
    destination_ip = received_message[45:56]
    message = received_message[56:]

    print("The packet received:\n Source MAC address: {source_mac}, Destination MAC address: {destination_mac}".format(
        source_mac=source_mac, destination_mac=destination_mac))

    print("\nSource IP address: {source_ip}, Destination IP address: {destination_ip}".format(source_ip=source_ip,
                                                                                              destination_ip=destination_ip))

    print("\n Message: " + message)

    ethernet_header = router3_mac #+ arp_table_mac[destination_ip]

    IP_header = source_ip + destination_ip

    packet = ethernet_header + IP_header + message
    router.send(received_message.encode("utf-8"))
    #destination_socket = arp_table_socket[destination_ip]

    #destination_socket.send(bytes(packet, "utf-8"))
    time.sleep(2)
    ack = router.recv(1024)
    ack = ack.decode("utf-8")
    print(ack)
    router.send(ack.encode("utf-8"))