#!/usr/bin/env python

from scapy.all import *
import sys, getopt, netifaces

ssidList = []

def sniffWifi(pkt):
	global ssidList
	if pkt.haslayer(Dot11Beacon):
		if pkt.addr2 not in ssidList:
			print pkt.sprintf("%Dot11.addr2%\t%Dot11.Beacon.info\t%Dot11Beacon.cap%")

			ssidList.append(pkt.addr3)

	elif pkt.haslayer(Dot11ProbeResp):
		if pkt.addr2 not in ssidList:
			print pkt.sprintf("%Dot11.addr2%\t%Dot11ProbeResp.info%\t%Dot11ProbeResp.cap%")
	                ssidList.append(pkt.addr3)
	else:
		print "Interface not specified or does not exist"

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "h")
	except getopt.GetoptError:
		print "CLI shoul look like: sudo python wifiSniffer.py <interface>"
		sys.exit(2)
		
	for opt, arg in opts:
		if opt in ("-h"):
			print "CLI shoul look like: sudo python wifiSniffer.py <interface"
			sys.exit()
	if (len(args)>0) and (args[0] in netifaces.interfaces()):
		sniff(iface=args[0], prn=sniffWifi, store=0)
	else:
		print "Interface not found"

	
if __name__ == "__main__":
	main(sys.argv[1:])




