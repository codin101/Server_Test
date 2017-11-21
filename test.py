#!/usr/bin/python

sdf
import os
import subprocess
import smtplib

mail = smtplib.SMTP("localhost")
r = "Patrick.Eff@motorolasolutions.com"
s = "Patrick.Eff@motorolasolutions.com"

d = open("errors.html","r")
msg = d.read()
mail.sendmail(s,r,msg)

	
#r = os.system("ping -c 2 " + "google.com" + " 2>/dev/null >/dev/null")

#if r == 0:
#	print "Up"
#else:
#	print "Down"


