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

    htmlFile.write("<html><head><link rel='stylesheet' type='text/css' href='style.css'>")
    htmlFile.write("<title>Build Servers Offline</title></head>")

    for i in failList:
	
	hostName = i.getHostName()

	if not i.getPorts():
		
		htmlFile.write("<div class='navbar'><div class='dropdown'>")
		htmlFile.write("<button class='dropbtn'><font color='red'>")
		htmlFile.write(hostName)
		htmlFile.write("</font><i class='fa fa-caret-down'></i>")
		htmlFile.write("</button><div class='dropdown-content'>")
		htmlFile.write("<p>Cannot Reach Server!</p></div></div></div>")
	else:
		htmlFile.write("<div class='navbar'><div class='dropdown'>")
		htmlFile.write("<button class='dropbtn'><font color='yellow'>")
		htmlFile.write(hostName)
		htmlFile.write("</font><i class='fa fa-caret-down'></i></button>")
		htmlFile.write("<div class='dropdown-content'>")
		for j in i.getPorts():
			
			htmlFile.write("<p>Port: " + str(j) + " is down</p>")
			
		htmlFile.write("</div></div></div>")
	
	htmlFile.write("</body></html>")
	

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
		
		sockFd.close()

	if failedPorts:
		failList.append(Node(hostName,failedPorts))
	
    if failList:
    	emailFailList(failList)

########## MAIN ##########

XML_FILE = sys.argv[1]
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
