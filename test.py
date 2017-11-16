#!/usr/bin/python

import os
import subprocess

#h = "google.com"
#r = os.system("ping -c 2 %s" %h)

r = os.system("ping -c 2 " + "google.com" + " 2>/dev/null >/dev/null")

if r == 0:
	print "Up"
else:
	print "Down"


