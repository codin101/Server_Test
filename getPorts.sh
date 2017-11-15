#!/bin/bash

logFile="open_ports.txt"

# greppin' n' steppin'
# awk'in   n' sqawkin'
# sed'in   n' forgettin'

# rock n roll :)/

if [ -e $logFile ] ; then rm -rf $logFile ; fi 

while read server
 do
 printf "===========$server==========\n" >>  $logFile ;

nmap -sS -Pn $server| grep -i open | awk -F " " '{print $1 $3}' \
	| 
while read line ; do  printf "$line" | sed -E 's/\/(tcp|udp)/,/g' | xargs echo >> $logFile ; done

done < file.txt
