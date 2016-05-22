#!/usr/bin/env python

import socket, struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("enp0s3", socket.htons(0x0800)))

packet = struct.pack("!6s6s2s", "\xaa\xaa\xaa\xaa\xaa\xaa",
"\xbb\xbb\xbb\xbb\xbb\xbb", "\x08\x00")

rawSocket.send(packet + "Hello World")
