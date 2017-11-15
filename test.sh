#!/bin/bash

<<<<<<< .merge_file_x8kAeW
logFile="open_ports";

while read line
 do
  printf "$line: " >> $logFile ;
  nmap -sS $line | grep open | awk -F " " '{print $1 $3}' | sed -E 's/\/(tcp|udp)//g' | printf " " >> $logFile
  printf "\n" >> $logFile;
 done < servers
=======
startTime=$(date +%s)
./check_server.py
endTime=$(date +%s)

duration=$(($endTime - $startTime))

echo "Run time: $duration second(s)"
>>>>>>> .merge_file_uDJGeR

