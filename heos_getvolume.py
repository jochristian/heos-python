#!/usr/bin/env python 
import socket
import re

TCP_IP = '192.168.150.17'
TCP_PORT = 1255
BUFFER_SIZE = 1024
MESSAGE = "heos://player/get_volume?pid=801392798"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

#print "received data:", data
match = re.search('level=([^"}]+)',data)
volume = match.group(1)
print (volume)
