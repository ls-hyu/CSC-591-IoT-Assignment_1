import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import sys
from datetime import datetime
import traceback
#from scapy.all import *

count = 0

def on_message(client, userdata, message):
    try:
        print("Message received!")
    except:
        traceback.print_exc()

mqttBroker = "raspberrypi"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 
file = sys.stdin.buffer.read(1024*1024*256)

while count < 50000:
    randNumber = uniform(20.0, 21.0)
    client.subscribe("#", qos=2)

    with open("time.txt", "a") as f:
        f.write("Send: " + str(datetime.now()) + "\n")
    client.publish("TEMPERATURE", file, qos=2)
    client.loop()
    client.loop_start()
    client.on_message=on_message
    client.loop_stop()
    print("SENT")
    count += 1
    print(count)
