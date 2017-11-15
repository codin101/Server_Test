#!/usr/bin/python

import sys
import socket
import xml.etree.ElementTree as ET

XML_FILE = "open.xml" 
errorFD = open("errors.txt","w")
tree = ET.parse(XML_FILE)
root = tree.getroot()

class Node:

	def __init__(self,hostName,port):
		self.hostName = hostName
		self.port = port

	def getHostName(self):
		return self.hostName

	def getPort(self):
		return self.port

def logError(hostName,port):

	errorFD.write("Failed to connect to: %s:%s\n" %(hostName,port))

############ MAIN ##############

aList = []
for node in root:

	hostName = node.get("hostname")
	ipAddr = socket.gethostbyname(hostName)

	for i in node.iter("port"):

		port = int(i.text)
		sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sockFD.settimeout(3)

		aNode = Node(hostName,port)
		try:

			sockFD.connect((ipAddr,port))
			print "Connected to %s:%s" %(hostName,port)
		except:
			aList.append(aNode)

		sockFD.close()

errorFD.close()
#if len(aList) > 0:

for element in aList:
	print "Connection Failed on %s:%s" %(element.getHostName(),element.getPort())
