#!/usr/bin/python

import sys
import socket
import xml.etree.ElementTree as ET

xmlFile = "open.xml" 
errorFD = open("errors.txt","w")

tree = ET.parse(xmlFile)
root = tree.getroot()

def logError(a,b):

	outFD.write("Could not connect to: ",a,b)

######### MAIN #########

for node in root:

	hostName = node.get("hostname")
	ipAddr = socket.gethostbyname(hostName)

	for i in node.iter("port"):

		port = int(i.text)
		sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sockFD.settimeout(3)

		try:

			sockFD.connect((ipAddr,port))
			print "Connected to: ", hostName,port
			#sockFD.close()

		except:
			logError(hostName,port)

		sockFD.close()



outFD.close()
