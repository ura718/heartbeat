#!/usr/bin/python

import smtplib


sender = 'nagios2'
receivers = ['ym26@nyu.edu']


message = """From: Nagios <nagios@nagios2.bobst.nyu.edu>
To: Systems <ym26@nyu.edu>
Subject: Alert from nagios2

Heartbeat Timeout
"""

try:
  smtpObj = smtplib.SMTP('mail.library.nyu.edu', 25)
  smtpObj.sendmail(sender, receivers, message)
  print "Successfully sent email"
except smtplib.SMTPException:
  print "Error: unable to send email" 


