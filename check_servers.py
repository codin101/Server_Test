#!/usr/bin/python

###### Motorola Solutions #######
#				#	
#	Author: Patrick Eff	#
#	Date: 11/15/2017	#
#				#
#################################

import sys
import socket
import xml.etree.ElementTree as ET

class Node:

	def __init__(self,hostName,port):
		self.hostName = hostName
		self.port = port
	def getHostName(self):
		return self.hostName
	def getPort(self):
		return self.port

def generateEmail(aList):
	fd = open("error.txt","w")
	for element in aList:
		fd.write("Connection Failed on %s:%s\n" %(element.getHostName(),element.getPort()))
	fd.close()	
	

############ MAIN ##############

exitCode = 0
XML_FILE = "servers.xml" 
tree = ET.parse(XML_FILE)
root = tree.getroot()


aList = []
for node in root:

	hostName = node.get("hostname")
	
	try:
		ipAddr = socket.gethostbyname(hostName)
	except:
		print "Failed to resolve hostname %s" %(hostName)
		continue

	for i in node.iter("port"):

		port = int(i.text)
		aNode = Node(hostName,port)

		sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sockFD.settimeout(3)

		try:
			sockFD.connect((ipAddr,port))
			print "Connected to %s:%s" %(hostName,port)
		except:
			aList.append(aNode)
			exitCode = 1

		sockFD.close()

if len(aList) > 0:
	generateEmail(aList)
else:
	print "Successfully connected to all servers"

sys.exit(exitCode)
