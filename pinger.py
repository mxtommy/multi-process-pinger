#!/usr/bin/env python

from pythonping import ping
import paho.mqtt.client as mqtt
import time
import sys
import re
import json

host = sys.argv[1]
descr = sys.argv[2]


client = mqtt.Client("Pinger "+ host)
client.connect("localhost")



while (True):

    result = str(ping(host, count=1, timeout=0.5))
    #split it into newline list
    lines = result.split("\n")

    numOk = 0
    allOk = False
    rtt = ""
    for line in lines:
        #test if Ok    
        if ("Reply from" in line):
            numOk += 1

        if ("Round Trip" in line):
            matchObj = re.search("([0-9.]+\/[0-9.]+\/[0-9.]+)", line)
            if (matchObj):
                rtt = matchObj.group(1)
    
    if (numOk == 1):
        allOk = True

    resp = {
        'host': host,
        'description': descr,
        'raw': result,
        'numOk': numOk,
        'rtt': rtt,
        'ok': allOk
    }

    client.publish("ping/"+ host, json.dumps(resp))
    print (host + " " + str(allOk))
    time.sleep (0.1)
