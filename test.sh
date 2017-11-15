#!/bin/bash

startTime=$(date +%s)
./check_server.py
endTime=$(date +%s)

duration=$(($endTime - $startTime))

echo "Run time: $duration second(s)"

