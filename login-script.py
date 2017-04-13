# -*- coding: utf-8 -*-

from ictf import iCTF
import os

# i=iCTF("http://35.161.233.76/")
i=iCTF("http://52.34.158.221/")

t=i.login("team1@example.com","password")

key_info = t.get_ssh_keys()

with open("ctf_key", 'wb') as f:
	f.write(key_info['ctf_key'])

with open("root_key", 'wb') as f:
	f.write(key_info['root_key'])

print key_info['ip']
print key_info['port']

os.system("chmod 600 ctf_key")
os.system("chmod 600 root_key")

ssh_string = "ssh -i ctf_key ctf@{0} -p {1}".format(key_info['ip'],key_info['port'])

os.system(ssh_string)