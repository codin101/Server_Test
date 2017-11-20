#!/usr/bin/python

import os
import sys
import socket
import xml.etree.ElementTree as ET

global exitCode
exitCode = 0

class Node:

    def __init__(self,hostName, portList = None):
        self.hostName = hostName
        self.portList = portList
    
    def getHostName(self):
        return self.hostName

    def getPorts(self):
        return self.portList


def emailFailList(failList):

    global exitCode
    exitCode = 1
	
    htmlFile = open("errors.html","w")

    buff = []
    buff.append(str("<html><head><link rel='stylesheet' type='text/css' href='style.css'>"))
    buff.append(str("<title>Build Servers Offline</title></head>"))

    b = []
    for i in failList:
	aBuff = ""
	if not i.getPorts():
		hostName = i.getHostName()
		buff.append(str("<div class='navbar'><div class='dropdown'>"))
		buff.append(str("<button class='dropbtn'><font color='red'>"))
		buff.append(str("</font><i class='fa fa-caret-down'></i>"))
		buff.append(str("</button><div class='dropdown-content'>"))
		buff.append(str("<p>Failed to Resolve Hostname</p></div></div></div>"))
	else:
		for j in i.getPorts():
			print i.getHostName() + ":" + str(j)

	
	buff.append(str("</body></html>"))
	
	htmlFile.write(str(buff))

def checkServers(nodeList):

    failList = []
    for e in nodeList:

	hostName = e.getHostName()
	portList = e.getPorts()

	try:
		ipAddr = socket.gethostbyname(hostName)
	except:
		failList.append(Node(hostName,None))
		continue
	
	failedPorts = []	
	for port in portList:
		
		sockFd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sockFd.settimeout(3)
		
		try:
			sockFd.connect((ipAddr,port))
		except:
			failedPorts.append(port)
	
	if failedPorts:
		failList.append(Node(hostName,failedPorts))
	
    if failList:
    	emailFailList(failList)

########## MAIN ##########

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


checkServers(nodeList)

sys.exit(exitCode)
