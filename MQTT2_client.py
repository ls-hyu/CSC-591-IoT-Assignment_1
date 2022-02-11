import paho.mqtt.client as mqtt
import time
from datetime import datetime
import sys
import subprocess

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    file = message.payload
    sys.stdout.buffer.write(file)
    with open("time.txt", "a") as f:
        f.write("Receive: " + time.ctime() + "\n")
#print(time.time())
#print(datetime.now())
#mqttBroker ="mqtt.eclipseprojects.io"
#mqttBroker = "raspberrypi"
#mqttBroker = "34.68.50.129"
mqttBroker = "127.0.0.1"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker) 
client.loop_start()
client.subscribe("TEMPERATURE", qos=2)
client.on_message=on_message

time.sleep(30)
client.loop_stop()