from random import randint
from socket import *
import time
import struct

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("The server is ready to receive on port: 12000")

while True:
	message, address = serverSocket.recvfrom(100)
	t=time.time()
	message = struct.unpack('i', message)
	rand = randint(0,10)
	if rand > 4:
		msg = struct.pack('id',message[0], t)
		print("Responding to ping request with sequence number", message[0], "received at", t)
		serverSocket.sendto(msg, address)
	else:
		print("Message with sequence number", message[0], "dropped")
