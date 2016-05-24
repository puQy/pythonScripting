#!/usr/bin/env python

from scapy.all import *
import netaddr
import netifaces
import pprint

iface = 'enp0s3'
addrs = netifaces.ifaddresses(iface)

infos = addrs[netifaces.AF_INET][0]
addr = infos['addr']
netmask = infos['netmask']
#https://pythonhosted.org/netaddr/tutorial_01.html
cidr = netaddr.IPNetwork('%s/%s' %(addr,netmask))

for ip in cidr:
	arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(ip), hwdst="ff:ff:ff:ff:ff:ff")
	arpResponse = srp1(arpRequest, timeout=1, verbose=0)
	if arpResponse:
		print "IP: " +arpResponse.psrc + "MAC: " + arpResponse.hwsrc 
	
