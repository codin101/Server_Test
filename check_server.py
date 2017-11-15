#!/usr/bin/python

import socket
import xml.etree.ElementTree as ET

xmlFile = "open.xml" 

tree = ET.parse(xmlFile)
root = tree.getroot()

for child in root:
    # we have a child
    # now,...... access the child's attribute ( it should be a <node> )
    hostName = child.attrib ## This is 'hostname="wbal.com" -> will print "wbal.com"
    # for each child, print their elements
    for i in child.iter("port"):
        port = int(i.text)
        sockFD = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ipBinary = socgethostbyname(hostName)
        sockFD.connect(ipBinary,port)
