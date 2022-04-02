#Client that will connect to server through routers.
import socket
import time
client_ip = "192.168.1.2"
client_mac = "12:AB:6A:BA:DD:C6"

router1 = ("LocalHost", 2000)
router2 = ("LocalHost", 2001)

client = socket.socket(AF_INET, socket.SOCK_STREAM)

client.connect(router1) #not created yet but waiting to merge code.