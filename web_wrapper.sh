#!/bin/bash
# set n to 1
n=1

# continue until $n equals 5
while [ $n -le 500 ]
do
	/root/code/attack_web
	sleep 2m
	n=$(( n+1 ))	 # increments $n
done