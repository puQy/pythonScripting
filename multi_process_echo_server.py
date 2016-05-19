#!/usr/bin/env python

import socket
import multiprocessing
import signal
import sys

def worker(client):
	data = 'dummy'
	while len(data):
		data = client.recv(2048)
		print "Client sent: " + data
		client.send(data)
	
	print "Connection closed.."
	client.close()
	
def ctrlcHandler(signum, frame):
	print "Shutting down server...:"
	tcp_socket.close()
	sys.exit(0)

signal.signal(signal.SIGINT, ctrlcHandler)

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsocket.bind(('localhost', 8000,))
tcpsocket.listen(10)

while True:
	print "Waiting for client request...."
	(conn,address) = tcpsocket.accept()
	
	print "MultiProcessEchoServer receive connection from: ", address
	print "Starting Echoing: ", address
	p = multiprocessing.Process(target=worker, args=(conn,))
	p.start()

