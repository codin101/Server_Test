#!/bin/bash

logFile="open_ports";

while read server
 do
 printf "===========$server==========\n" >>  $logFile ;
nmap -sS $server| grep open | awk -F " " '{print $1 $3}' |
while read line
 do
  printf "$line" | sed -E 's/\/(tcp|udp)/,/g' | xargs echo >> $logFile ;
 done
done < servers.txt
