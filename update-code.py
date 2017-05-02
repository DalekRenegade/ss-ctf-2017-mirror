#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

cmd = "scp -r -P 1345 -i root_key ../. root@52.88.7.244:code"
os.system(cmd)