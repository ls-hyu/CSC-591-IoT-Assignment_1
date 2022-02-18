
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import sys
import subprocess
import os
from pathlib import Path
import traceback



count = 0

def on_message(client, userdata, message):
    
    global count
    try:
        with open("time.txt", "a") as f:
            f.write("Receive: " + str(datetime.now()) + "\n")
            count += 1
    except:
        pass
    file = message.payload
    
    content = file
    if count <= 1:
        sys.stdout.buffer.write(file)
    
mqttBroker = "raspberrypi"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)
outputFile = "output.txt"
client.subscribe("TEMPERATURE", qos=2)

while count < 10:
    client.loop_start()
    client.on_message=on_message
    client.loop_stop()