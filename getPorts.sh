#!/bin/bash

logFile="open_ports.txt"

# awk'in   n' sqawkin'
# greppin' n' steppin'
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
