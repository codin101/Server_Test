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
import string
import smtplib
import datetime
import subprocess
import xml.etree.ElementTree as ET

global exitCode
global emailMsg

exitCode = 0
emailMsg = ""

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

def sendEmail():

    global emailMsg

    mail = smtplib.SMTP("localhost")

    now = datetime.datetime.now()

    day = "%d" % now.day
    year = "%d" % now.year
    month = "%d" % now.month
  
    sender = "flscm@motorolasolutions.com"
    recv = "Patrick.Eff@motorolasolutions.com"
    subject = "[ Jenkins ] Environment Test Results: "
    if exitCode == 1:
	subject += "FAILED"
    else:
	subject += "PASSED"

    emailMsg += "</body></html>\n"

    header = "From: " + sender + "\nTo: " + recv + "\nSubject: " + subject  + " " + month + "/" + day + "/" + year + "\nContent-type: text/html\n"
    body = header + emailMsg + "\r\n"

    mail.sendmail(sender,recv,body)

# Makes a connect() system call to each IP:Port ( IPv4 )
def attemptConnections(nodeList):

    global exitCode
    global emailMsg

    emailMsg = """
	  <html><head><style type="text/css">
	  .summary td.success{
              background: #bef0bc;
	   }
	   .summary td.error {
             background: #f7cfcf;
	   }
	  </style></head>
	  """

    emailMsg += "<body>NOTE: This email has been automatically generated. Please DO NOT reply.<br><br>"
    emailMsg += "To view this job in Jenkins please go to: https://fl08jenkins.mot-solutions.com:8443/view/CM_Team/job/Check_Build_Servers_Online/<br><br>"
    emailMsg += "<b>Task: Check Build Servers Online</b>"
    emailMsg += "<div class=summary><table><tr><th bgcolor='grey'>Server</th><th bgcolor='grey'>Status</th></tr>"

    failList = []
    for e in nodeList:

	hostName = e.getHostName()
	portList = e.getPorts()

	try:
		ipAddr = socket.gethostbyname(hostName)
	except:
		exitCode = 1
		emailMsg += "\n<tr><td class=\"error\">" + hostName + "</td><td class=\"error\">Failed to resolve hostname</td></tr>\n"
		continue
	
	failedPorts = []	
	for port in portList:
		
		sockFd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sockFd.settimeout(3)
		
		try:
			sockFd.connect((ipAddr,port))
		except:
			exitCode = 1
			failedPorts.append(port)
		
		sockFd.close()
	
	if not failedPorts:

		emailMsg += "\n<tr><td class=\"success\">" + hostName + "</td><td class=\"success\">PASS</td></tr>\n"
	else:
	
		emailMsg += "\n<tr><td class=\"error\">" + hostName + "</td><td class=\"error\">\n"
		for port in failedPorts:
			emailMsg += "Port " + str(port) + " is closed<br>"

		emailMsg += "\n</td></tr>\n"

    emailMsg += "\n</div></table>"
 

def checkServersOnline(XML_FILE):

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    nodeList = []
    for node in root:

        hostName = node.get("hostname")

        portList = []
	for i in node.iter("port"):

		port = int(i.text)
		portList.append(port)
	
	aNode = Node(hostName,portList)
	nodeList.append(aNode)

    attemptConnections(nodeList)


def checkBuildCompiles():

    global emailMsg
    global exitCode

    cwd = os.getcwd()

    PATH = os.environ["PATH"]
    NEW_PATH = "/local_data/tools/bin:%s" % PATH

    os.environ["PATH"] = NEW_PATH

    cmd = """
	rm -rf build ;
	mkdir build ;
	cd build ;
	export PATH="/local_data/tools/bin:$PATH" ;
	git clone ssh://git@bitbucket.mot-solutions.com:7999/astro_sub/apx.git ;
	cd apx ;
	git checkout -b env_test_branch origin/fl08_sr7_17_mackinaw_main ;
	cd discovery/code ;
	source ./build_env ;
	emake disc_por_all | tail -5;
	"""

    cmd = """
	cd build;
	cd apx;
	cd discovery/code ;
	source ./build_env ;
	emake disc_por_all | tail -5;
	"""

    job = subprocess.Popen(['/bin/bash','-c',cmd],stdout=subprocess.PIPE)
    job.wait() # waitpid()

    output = cwd + "/build/" + "apx/discovery/code/host/portable/output/bin/Discovery_Por_Host_arm9.bbf"

    emailMsg += "<br><b>Task: Check Build Compiles</b>"
    emailMsg += "<div class=summary><table><tr><th bgcolor='grey'>Build Test</th><th bgcolor='grey'>Status</th></tr>"
    emailMsg += "<tr>"

    logs = job.stdout.read()

    if os.path.exists(output):

	emailMsg += "<td class=\"success\">Discovery_Por_Host_arm9.bbf</td>"
	emailMsg += "<td class=\"success\">" + logs + "</td>"

    else:

	exitCode = 1	
	emailMsg += "<td class=\"error\">Discovery_Por_Host_arm9.bbf</td>"
	emailMsg += "<td class=\"error\">" + logs + "</td>"
    
  
    emailMsg += "</tr></table>"
    emailMsg += "</p>"

########################## MAIN ###########################

numArgs = len(sys.argv)

if numArgs != 2:
	print "usage: ./check_servers.py <servers.xml>"
	sys.exit(1)

XML_FILE = sys.argv[1]

checkServersOnline(XML_FILE)
checkBuildCompiles()
sendEmail()

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

