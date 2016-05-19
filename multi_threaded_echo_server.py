#!/usr/bin/env python

import socket
import threading
import sys
import signal

class WorkerThread(threading.Thread):
	def __init__(self, client):
		threading.Thread.__init__(self)
		self.client = client

	def run(self):
		data = 'dummy'
		while len(data):
			data = self.client.recv(2048)
			print "Client sent: ", data
			self.client.send(data)

		print "Closing connection..."

def ctrlHandler(signum, frame):
	print "Shutting down server ...."
	tcpsocket.close()
	sys.exit(0)

signal.signal(signal.SIGINT, ctrlHandler)
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsocket.bind(('localhost', 8000,))
tcpsocket.listen(10)

while True:
	print "Waiting for a client...."
	(client,(ip,port)) = tcpsocket.accept()

	print "Received connection from client: ", ip, port
	print "Starting conversation...", client
	
	worker = WorkerThread(client)
	worker.setDaemon(True)
	worker.start()
