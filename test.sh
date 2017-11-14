#!/bin/bash

logFile="open_ports";

while read line
 do
  printf "$line: " >> $logFile ;
  nmap -sS $line | grep open | awk -F " " '{print $1 $3}' | sed -E 's/\/(tcp|udp)//g' | printf " " >> $logFile
  printf "\n" >> $logFile;
 done < servers

