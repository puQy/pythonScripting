#!/usr/bin/env python

import SocketServer, http.server

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path=="/admin":
			self.wfile.write("This page is only for Admins!")
		else:
			http.server.SimpleHTTPReqestHandler.do_GET(self)

httpServer = SockerServer.TCPServer(('localhost', 8000), HttpRequestHandler)

httpServer.server_name='localhost'
httpServer.server_port=20000
httpServer.serve_forever
