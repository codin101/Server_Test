#!/usr/bin/python

################################################################################
#
#                  P Y T H O N   S P E C I F I C A T I O N
#             COPYRIGHT 2017 MOTOROLA, INC. ALL RIGHTS RESERVED.
#                    MOTOROLA CONFIDENTIAL PROPRIETARY
#
################################################################################
#
# FILE NAME: check_servers.py
#
#---------------------------------- PURPOSE ------------------------------------
# 
#  Check all the build servers found in servers.xml are online.
#  Jenkins will send an email if any ports or servers are offline.
# 
#--------------------------- PROJECT SPECIFIC DATA -----------------------------
# 
#
#----------------------------- MODULE INCLUDES ---------------------------------

################################################################################

import os
import sys
import socket
import smtplib
import xml.etree.ElementTree as ET

global exitCode
exitCode = 0

# Node class:
# Node has a hostName and dynamic array of ports
class Node:

    def __init__(self,hostName, portList = None):
        self.hostName = hostName
        self.portList = portList
    
    def getHostName(self):
        return self.hostName

    def getPorts(self):
        return self.portList


def showFailures(failList):

    global exitCode
    exitCode = 1

    mail = smtplib.SMTP("localhost")
    r = "Patrick.Eff@motorolasolutions.com"
    s = "Patrick.Eff@motorolasolutions.com"

    msg = ""
    for i in failList:

	portList = i.getPorts()
	hostName = i.getHostName()

	if not portList:
		msg+= "Failed to Resolve Host: " + hostName  + "\n"
		continue 
	else:
		for j in portList:
			msg+= "Failed to connect to " + hostName + ":" + str(j) + "\n"

    mail.sendmail(s,r,msg)

# Makes a connect() system call to each IP:Port ( IPv4 )
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
    	showFailures(failList)

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

################################################################################
#
#                              HISTORY
#
################################################################################
#
# 11/21/2017	Patrick Eff  	Initial Creation
#
################################################################################

