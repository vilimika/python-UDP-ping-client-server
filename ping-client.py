import time
from socket import *
import sys
import struct

def avg_min_max(values):
	rtrn={}
	rtrn['min']=min(values)
	rtrn['max']=max(values)
	rtrn['avg']=sum(values)/len(values)
	return rtrn
 
if len(sys.argv) != 3:
	print("Usage: PingClient <server ip address> <server port no>")
	sys.exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
addr = (ip, port)
print('Pinging' , ip, port)
timeouts=0
rtt_list=[]
ott_list=[]
for pings in range(1,11):
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.settimeout(1) 
	message = struct.pack('i', pings)	
	start = time.time()
	clientSocket.sendto(message, addr)
	try:
		data, server = clientSocket.recvfrom(1024)
		end = time.time()
		rtt = round(end - start, 6)
		msg_recv = struct.unpack('id', data)
		ott = round(msg_recv[1] - start , 6)
		ott_list.append(ott)
		rtt_list.append(rtt)
		print('Ping message number', pings, 'RTT OTT','%f' %  rtt,'%f' % ott, 'secs')
	except timeout:
		timeouts = timeouts + 1
		print('Ping message number',pings, 'timed out')

rtt=avg_min_max(rtt_list)
ott=avg_min_max(ott_list)
print('Number of packets sent', pings)
print('Number of packets received', pings - timeouts)
print('Number of packets lost', timeouts)
print('Percent of packets lost', timeouts/pings*100)
print('RTT average, max, min times', rtt['avg'], rtt['max'], rtt['min'], 'secs')
print('OTT average, max, min times','%f' % ott['avg'],'%f' %  ott['max'],'%f' % ott['min'], 'secs')
