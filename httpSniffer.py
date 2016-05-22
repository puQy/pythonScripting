#!/usr/bin/env python

from scapy.all import *

def printHttpHeadersAndData(pkt):
	payload = pkt.sprintf("%Raw.load%")
	print pkt.summary()
	
	if payload.startswith("'GET") or payload.startswith("'POST"):
		data = payload[1:-1].split("\\r\\n")
		a = data[0].split()
		print "GET/POST data: ",a[1]
		del data[0]
	elif payload.startswith("'HTTP"):
		data = payload[1:-1].split("\\r\\n")
		del data[0]
		for item in data:
			print item
	print "###############################################"

sniff(filter="tcp port 80", prn=printHttpHeadersAndData, store=0)
