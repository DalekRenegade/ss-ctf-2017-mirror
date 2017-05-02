#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
from ictf import iCTF
from sys import argv

argc = len(argv)

with open("secret.txt", 'r') as f:
	username = f.readline().strip()
	passwd = f.readline().strip()

if username == "":
	print "You forgot to copy credentials from the email..."
	print "Create a file named 'secret.txt' in the finals directory and put first line as username and second line as passwd."
	exit(0)

i = iCTF("http://35.160.215.67/")
t = i.login(username,passwd)

option = input("Enter one of these: \n1: services\n2: targets\n")

if option == 1:
	services = t.get_service_list();
	for service in services:
		print "*******"
		print "name\t: {0}".format(service['service_name'])
		print "state\t: {0}".format(service['state'])
		print "port\t: {0}".format(service['port'])
		print "description\t: {0}".format(service['description'])

elif option == 2:
	service = raw_input("Which service: ")
	targets = t.get_targets(service)['targets']

	for target in targets:
		print "*********"
		print "Hostname:\t{0}".format(target['hostname'])
		print "PORT: \t\t{0}".format(target['port'])
		print "flag_id: \t{0}".format(target['flag_id'])
		print "team name: \t{0}".format(target['team_name'])