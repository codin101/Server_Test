#!/usr/bin/python

import os
import subprocess
import smtplib

mail = smtplib.SMTP("localhost")
msg = "<html><head><title>Fail</title></head></html>"
r = "Patrick.Eff@motorolasolutions.com"
s = "Patrick.Eff@motorolasolutions.com"

mail.sendmail(s,r,msg)

	
#r = os.system("ping -c 2 " + "google.com" + " 2>/dev/null >/dev/null")

#if r == 0:
#	print "Up"
#else:
#	print "Down"


