#!/usr/bin/env python

import SocketServer, threading

class ThreadedEchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "Connetion from: ", self.client_address
		data = 'dummy'
		while len(data):
			data = self.request.recv(4096)
			print "Client sent: ", data
			self.request.send(data)

		print "Client left..."

class ThreadedEchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass


serverAddress= ('localhost', 8888)

server = ThreadedEchoServer(serverAddress, ThreadedEchoHandler)

t = threading.Thread(target=server.serve_forever)
t.setDaemon=True
t.start()
