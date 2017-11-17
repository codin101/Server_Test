#!/usr/bin/python

import sys
import socket
import xml.etree.ElementTree as ET

class Node:

	def __init__(self,hostName,portList=None):
		self.hostName = hostName
		self.ports = portList or []

	def getHostName(self):
		return self.hostName

	def getPorts(self):
		return self.ports


exitCode = 0
XML_FILE = "servers.xml"
tree = ET.parse(XML_FILE)
root = tree.getroot()

nodeList= []
for node in root:

	hostName = node.get("hostname")
	
	portList = []
	for i in node.iter("port"):

		port = int(i.text)
		portList.append(port)
	
	aNode = Node(hostName,portList)
	nodeList.append(aNode)
	

for i in nodeList:
	print 




sys.exit(exitCode)
