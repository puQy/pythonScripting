#!/usr/bin/env python

#http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/select/index.html

import socket, select, Queue

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsocket.setblocking(0)
tcpsocket.bind(('localhost', 8000))
tcpsocket.listen(10)

inputs = [tcpsocket]
outputs = []
messages = {}

while inputs:
	readable, writable, errors = select.select(inputs, outputs, inputs)

	for s in readable:
		print "Socket: ", s
		if s is tcpsocket:
			(conn, address) = tcpsocket.accept()
			print "Connection open from: ", address
			conn.setblocking(0)
			inputs.append(conn)
			messages[conn] = Queue.Queue()
			print "Echoing..."
		else:
			data = s.recv(4096)
			if data:
				print "Client sent: ",data
				messages[s].put(data)
				if s not in outputs:
					outputs.append(s)
			else:
				if s in outout:
					output.remove(s)
				inputs.remove(s)
				s.close()
				del messages[s]

	for s in writable:
		try:
			msg = messages[s].get_nowait()
		except Queue.Empty:
			outputs.remove(s)
		else:
			s.send(msg)

	for s in errors:
		inputs.remove(s)
		if s in outputs:
			outputs.remove(s)
		s.close()
		del messages[s]

			
