#!/usr/bin/python


import socket			
import time

message = "hello"
host = socket.gethostname()		# get hostname
port = 9977				# get port

s = socket.socket(socket.AF_INET,	# Internet
		socket.SOCK_DGRAM)	# UDP, create a socket object

while True:
  s.sendto(message, (host,port))
  time.sleep(3)
