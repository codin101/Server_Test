#!/bin/bash

startTime=$(date +%s)

./check_servers.py

endTime=$(date +%s)

duration=$(($endTime - $startTime))

echo "Run time: $duration second(s)"

