# -*- coding: utf-8 -*-

from ictf import iCTF
import os
from sys import argv

print "This is for Team 1:\n"

argc = len(argv)

i=iCTF("http://52.34.158.221/")
t=i.login("team1@example.com","password")

if argc == 1:
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