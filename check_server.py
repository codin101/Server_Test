#!/usr/bin/python

import sys
import socket
import xml.etree.ElementTree as ET

numErrors = 0
xmlFile = "open.xml" 
errorFD = open("errors.txt","w")
tree = ET.parse(xmlFile)
root = tree.getroot()

def logError(a,b):

	errorFd.write("%s",%(a,b))



############ MAIN ##############

for node in root:

	hostName = node.get("hostname")
	ipAddr = socket.gethostbyname(hostName)

	for i in node.iter("port"):

		port = int(i.text)
		sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sockFD.settimeout(3)

		try:

			sockFD.connect((ipAddr,port))
			print "Connected to %s:%s" %(hostName,port)
		except:
			logError(hostName,port)
			numErrors = numErrors + 1

		sockFD.close()

errorFD.close()
print "%s errors found" %(numErrors)
