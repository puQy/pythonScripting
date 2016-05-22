#!/usr/bin/env python

import socket
import struct
import binascii

IP, TCP, HTTP = False, False, False
  
def parseETH(pkt):
	ethHeader = struct.unpack("!6s6s2s", pkt)
	print "Source MAC-Addr: ", binascii.hexlify(ethHeader[1])
	print "Destination MAC-Addr: ",binascii.hexlify(ethHeader[0])
	
	global IP
	if binascii.hexlify(ethHeader[2]) == '0800':
		IP = True

def parseIP(pkt):
	#9bytes(version, length, type of sservice, total length, identification, flags, fragment offset, time to live
	#1byte(Protocol) 2byte(Header checksum, 2x 4byte( Source and Dest
	ipHeader = struct.unpack("!9s1s2s4s4s", pkt)
	print "Source Address is: ",ipHeader[3]
	print "Destination Address is: ",ipHeader[4]
 
	global TCP
	if binascii.hexlify(ipHeader[1]) == '06':
		TCP = True
	

def parseTCP(pkt):
	tcpPacket = struct.unpack("!HHLLBBHHH", pkt)
	if tcpPacket[0] == '80' or tcpPacket[1] == '80':
		global HTTP
		HTTP = True	
	
	print "Source Port: ", tcpPacket[0]
	print "Dest Port: ", tcpPacket[1]
	print "Sequence Number: ", tcpPacket[2]
	print "ACK Number: ", tcpPacket[3]
	print "Data-Offset: ", tcpPacket[4]
	print "flag: ", tcpPacket[5]
	print "window: ", tcpPacket[6]
	print "Checksum: ", tcpPacket[7]
	print "Urgent Pointer: ", tcpPacket[8]

def parseHTTP(data):
	print "HTTP Data: ", data

rawsocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while True:
	pkt = rawsocket.recvfrom(2048)
	IP, TCP, HTTP = False, False, False
	parseETH(pkt[0][0:14])
	
	if IP:
		parseIP(pkt[0][14:34])
	if TCP:
		parseTCP(pkt[0][34:54])
	if HTTP:
		parseHTTP(pkt[0][54:])

	print "##################################"
	

