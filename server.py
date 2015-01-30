#!/usr/bin/python

import socket
import select
import time
import smtplib


# Send email if heartbeat is not detected after 30 seconds

def SendEmail(timeout):
  sender = 'nagios2'
  receivers = ['ym26@nyu.edu']


  message = """From: Nagios <nagios@nagios2.bobst.nyu.edu>
To: Systems <ym26@nyu.edu>
Subject: Alert from nagios2

Heartbeat Timeout: %i
""" % (timeout)

  try:
    smtpObj = smtplib.SMTP('mail.library.nyu.edu', 25)
    smtpObj.sendmail(sender, receivers, message)
    print "Successfully sent email"
  except smtplib.SMTPException:
    print "Error: unable to send email"










def main():
  host = socket.gethostname()			# get hostname, or you can set it as '0.0.0.0' or dns
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
    socket1, wlist, elist  = select.select([s],[],[],30.0)		# creating a timeout session

    if [socket1, wlist, elist] == [ [], [], [] ]:
      runningtime = time.time()
      timeout = runningtime - starttime
      #print "Timeout detected. %i sec" % (int(timeout))
      SendEmail(timeout)

    else:
      data, addr = s.recvfrom(1024)			# buffer size is 1024 bytes
      print "Received message: ", data
      starttime = time.time()  



if __name__ == '__main__':
  main()

