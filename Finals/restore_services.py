#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
from sys import argv

print "Use: ./restore_services service1 service2 service3 ..."
argc = len(argv)

services = argv[1:] or ["sample_c", "sample_py", "sample_web"]

for service in services:
	cmd = "mkdir -p {0}; scp -r -P 1345 -i root_key ../{0} root@52.89.52.99:temp/{0}".format(service)
	os.system(cmd)

