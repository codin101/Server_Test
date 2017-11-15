#!/usr/bin/python

import socket
import xml.etree.ElementTree as ET

xmlFile = "open.xml" 

tree = ET.parse(xmlFile)
root = tree.getroot()

for node in root:
	hostName = node.get("hostname")
	print hostName
	for i in node.iter("port"):
		port = int(i.text)
		print port
