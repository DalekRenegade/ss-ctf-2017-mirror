#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from ictf import iCTF
import os
from sys import argv

argc = len(argv)

if not (argc > 2):
	print "Pass a subject and message! \n./support.py <subject> <message>"

if argc == 3:
	subject = argv[1]
	message = argv[2]

with open("secret.txt", 'r') as f:
	username = f.readline().strip()
	passwd = f.readline().strip()

if username == "":
	print "You forgot to copy credentials from the email..."
	print "Create a file named 'secret.txt' in the finals directory and put first line as username and second line as passwd."
	exit(0)

i = iCTF("http://35.167.152.77/")
t = i.login(username,passwd)

t.send_support_ticket(subject,message)