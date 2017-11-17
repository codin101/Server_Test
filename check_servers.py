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
	

	htmlFile = open("error.html","w")
	htmlFile.write("<html>\n<head>\n<title>Build Servers Status</title>\n</head>\n<body>")

	for element in aList:
		htmlFile.write("<p>Connection FAILED on %s:%s</p>" %(element.getHostName(),element.getPort()))

	htmlFile.write("</body></html>")
	

############ MAIN ##############

exitCode = 0
XML_FILE = "servers.xml" 
tree = ET.parse(XML_FILE)
root = tree.getroot()

htmlFile = open("status.html","w")
htmlFile.write("<html><head><title>Build Server Status</title></head><body>")
htmlFile.write("<table>")

# if ( connect -> Green, else Red )


aList = []
for node in root:

	hostName = node.get("hostname")
	htmlFile.write("<tr><th>" + str(hostName) )

	try:	
		ipAddr = socket.gethostbyname(hostName)
	except:
		print "Failed to resolve hostname %s" %(hostName)
		exitCode = 1
		continue 

	for i in node.iter("port"):

		port = int(i.text)
		aNode = Node(hostName,port)

		sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sockFD.settimeout(3)
		
		canConnect = 1
		try:
			sockFD.connect((ipAddr,port))
			#print "Connected to %s:%s" %(hostName,port)
		except:
			aList.append(aNode)
			canConnect = 0
			exitCode = 1

		sockFD.close()
		htmlFile.write("<td>")
		if( canConnect == 1 ):
			htmlFile.write("<font color='green'>" + str(port) + "</td>")

		else:
			htmlFile.write("<font color='red'>" + str(port) + "</td>")


	htmlFile.write("</tr></th>")

htmlFile.write("<table>")

#if len(aList) > 0:
#	generateEmail(aList)
#else:
#	print "Successfully connected to all servers"

sys.exit(exitCode)
