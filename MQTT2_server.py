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
        #global count
        #count += 1
        #print(count)
        print("!!!!!!!!!!!!!!!!!!!!!!!")
        #with open("time.txt", "a") as f:
        #    f.write("Send: " + str(datetime.now()) + "\n")
        #client.publish("TEMPERATURE", file, qos=2)
        #client.loop()
    except:
        traceback.print_exc()
    #print("received message: " ,str(message.payload.decode("utf-8")))

#mqttBroker ="mqtt.eclipseprojects.io" 
#mqttBroker = "10.2.1.255"
mqttBroker = "raspberrypi"
#mqttBroker = "34.68.50.129"
#mqttBroker = "34.68.50.129"
#mqttBroker = "10.2.1.129"
#mqttBroker = "127.0.0.1"
#port = 1883

#packets = sniff(filter = "host 127.0.0.1")

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 
#client.connect(mqttBroker, port)
#file = sys.stdin.buffer.read(1024*1024*256)
file = sys.stdin.buffer.read(1024*1024*256)
#time.sleep(10)
"""
client.subscribe("#", qos=2)

#time.sleep(10)
with open("time.txt", "a") as f:
    f.write("Send: " + str(datetime.now()) + "\n")
client.publish("TEMPERATURE", file, qos=2)
client.loop()

while count < 50:
    client.loop_start()
    client.on_message=on_message
    client.loop_stop()
    #print(count)
    #count += 1
    #print(count)

"""
#while True:
while count < 50000:
    #time.sleep(10)
    randNumber = uniform(20.0, 21.0)
    #file = sys.stdin.buffer.read(1024*1024)

    client.subscribe("#", qos=2)

    with open("time.txt", "a") as f:
        f.write("Send: " + str(datetime.now()) + "\n")
    #client.subscribe("#", qos=2)
    client.publish("TEMPERATURE", file, qos=2)
    client.loop()
    client.loop_start()
    client.on_message=on_message
    client.loop_stop()
    print("SENT")
    count += 1
    print(count)

"""
    with open("time.txt", "a") as f:
        client.subscribe("#", qos=2)
        client.publish("TEMPERATURE", file, qos=2)
        print("SENT")
        #client.loop()
        
        client.loop_start()
        client.on_message = on_message
        client.loop_stop()
        
        #f.write("Send: " + time.ctime() + "\n")
        f.write("Send: " + str(datetime.now()) + "\n")

    print(count)
    count += 1
    time.sleep(10)
    #print(packets)
"""