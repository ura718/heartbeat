#!/usr/bin/python

import socket
import select
import time

host = socket.gethostname()			# get hostname
port = 9977					# get port


s = socket.socket(socket.AF_INET,		# Internet
		  socket.SOCK_DGRAM)		# UDP, establish client connection

s.bind((host, port))				# bind host,port to socket



# Create initial start time count
starttime = time.time()


# socket1 = read event
# wlist = write event 
# elist = error event
# timeout
while True:
  socket1, wlist, elist  = select.select([s],[],[],6.0)		# creating a timeout session
  
 
  if [socket1, wlist, elist] == [ [], [], [] ]:
    runningtime = time.time()
    timeout = runningtime - starttime
    print "Timeout detected. %i sec" % (int(timeout))

  else:
    data, addr = s.recvfrom(1024)			# buffer size is 1024 bytes
    print "Received message: ", data
    starttime = time.time()  




