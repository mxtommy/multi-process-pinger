# Multi-process pinger

Simple Python pinger split across many processes with MQTT.

## Dependencies:
* Python Modules:
    * pythonping
    * paho MQTT client
* A MQTT Broker (I used mosquitto)


### Broker setup

* Install mosquitto broker
* Add following to end of C:\Program Files\mosquitto\mosquitto.conf (creates a websockets listener for webpage and mqtt listener for python scripts)
```
listener 9001
protocol websockets
listener 1883
protocol mqtt
```
* run broker: ./mosquitto.exe -c mosquitto.conf

### Launch pings

You can run the script against one host with "python pinger.py <IP> <DESCRIPTION>". Description should be only one word long. 

You can also create a list in 'list.txt' and run the 'launch.py' script. It uses the windows 'start' command to launch a new process for each target in list.

### Webpage

Included is a minimal index.html webpage. It connects over websocket to the mqtt broker and processes the messages received to show status of hosts. Note both webpage and ping scripts have localhost without authentication coded as mqtt broker, if that's not the case, needs updating :)

