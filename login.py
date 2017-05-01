#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from ictf import iCTF
import os
from sys import argv

argc = len(argv)

if argc > 1:
	user = argv[1]
else:
	user = "ctf"
	
with open("secret.txt", 'r') as f:
	username = f.readline().strip()
	passwd = f.readline().strip()

if username == "":
	print "You forgot to copy credentials from the email..."
	print "Create a file named 'secret.txt' in the finals directory and put first line as username and second line as passwd."
	exit(0)

i=iCTF("http://35.160.215.67/")

t = i.login(username,passwd)

key_info = t.get_ssh_keys()

with open("ctf_key", 'wb') as f:
	f.write(key_info['ctf_key'])

with open("root_key", 'wb') as f:
	f.write(key_info['root_key'])

print key_info['ip']
print key_info['port']

os.system("chmod 600 ctf_key")
os.system("chmod 600 root_key")

if user == 'root':
	ssh_string = "ssh -i root_key root@{0} -p {1}".format(key_info['ip'],key_info['port'])
else:
	ssh_string = "ssh -i ctf_key ctf@{0} -p {1}".format(key_info['ip'],key_info['port'])

os.system(ssh_string)


