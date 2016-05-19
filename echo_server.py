#!/usr/bin/env python

import socket

#create stream socket, AF_inet adress family internet
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
#set options sol_socket ist das socket layer und benutzt protocal unabhaengige  options
#wenn bspw eine option benutzt wird beschreibt sol_socket das diese in dem socket selbst gesucht werden soll
#http://pubs.opengroup.org/onlinepubs/7908799/xns/getsockopt.html

tcpsocket.bind(('localhost', 8000,)) #bindet den socket an eine ip und einen Port, (HOST,PORT) -tuple

tcpsocket.listen(10) #besagt wieviele anfragen der socket bearbeiten kann

print "Waiting for a client request..."

(client, (ip,port)) = tcpsocket.accept() #erstellt neuen sock welcher vom client benutzt wird gibt ein tuple (conn, address) zurueck

print "Received connection from: ", ip, port
print "Starting ECHO Server"

data = 'dummy'

while len(data):
	data = client.recv(2048)
	print "Client sent: " + data
	client.send(data)

print "Closing connection...."
client.close()

print "Shuting down server ..."

tcpsocket.close()
