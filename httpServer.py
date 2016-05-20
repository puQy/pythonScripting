#!/usr/bin/env python

import SocketServer, SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path=="/admin":
			self.wfile.write("This page is only for admins with permissions!")
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(('localhost',10000), HttpRequestHandler)

httpServer.serve_forever()
