#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

cmd = "scp -r -P 1345 -i root_key root@52.89.52.99:.ssh/authorized_keys ./authorized_keys"
os.system(cmd)
os.system("cat ~/.ssh/id_rsa.pub >> ./authorized_keys")
cmd = "scp -r -P 1345 -i root_key ./authorized_keys root@52.89.52.99:.ssh/authorized_keys"
os.system(cmd)