#!/usr/bin/env python

import re
import os
import time


#read targets
with open("list.txt") as f:
    targets_raw = f.readlines()
targets = {}

for line in targets_raw:
    matchObj = re.match("^(\S+)\t(\S+)",line)
    if matchObj:
        targets[matchObj.group(2)] = matchObj.group(1)

for target in targets:
    os.system("start pinger.py " + target + " " + targets[target])
