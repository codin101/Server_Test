#!/usr/bin/python

import os
import subprocess

#h = "google.com"
#r = os.system("ping -c 2 %s" %h)

class J:

	def __init__(self,h):
		self.h = h	
	def get(self):
		return self.h


a = J("sdf")
print a.get()
	
#r = os.system("ping -c 2 " + "google.com" + " 2>/dev/null >/dev/null")

#if r == 0:
#	print "Up"
#else:
#	print "Down"


