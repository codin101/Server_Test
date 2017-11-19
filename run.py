#!/usr/bin/python

import sys
import socket
import xml.etree.ElementTree as ET

global exitCode
exitCode = 0

# Node class has:
# hostName
# array of Ports

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

    for i in failList:

        hostName = i.getHostName()
        portList = i.getPorts()
        if not portList:
            print "Could not Resolve Host: " + hostName
        else:
            for j in portList:
                print "Could not connect to " + hostName + ":" + str(j)
        

def checkServers(nodeList):

    failList = []
    for e in nodeList:

        hostName = e.getHostName()

        try:
            ipAddr = socket.gethostbyname(hostName)
        except:
            failList.append(Node(hostName,None))
            continue 

        portList = []
        for port in e.getPorts():

                sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sockFD.settimeout(3)

                try:
                    sockFD.connect((ipAddr,port))
                except:
                    portList.append(port)


                sockFD.close()
        
        failList.append(Node(hostName,portList))

    if failList:
        emailFailList(failList)

#### MAIN ####

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
