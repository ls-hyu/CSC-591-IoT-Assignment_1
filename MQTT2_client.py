
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import sys
import subprocess
import os
from pathlib import Path
import traceback


#output = sys.argv[3]
count = 0

def on_message(client, userdata, message):
    #print("received message: " ,str(message.payload.decode("utf-8")))
    global count
    try:
        with open("time.txt", "a") as f:
            #f.write("Receive: " + time.ctime() + "\n")
            f.write("Receive: " + str(datetime.now()) + "\n")
            count += 1
    except:
        pass
    file = message.payload
    #sys.stdout.buffer.write(file)
    content = file
    #sys.stdout.buffer.write(file)
    if count <= 1:
        sys.stdout.buffer.write(file)
    """
    if count >= 1:
        #sys.stdout.buffer.write(file)
        #sys.stdout.flush()
        pass
    else:
        #sys.stdout.flush()
        try:
            sys.stdout.buffer.write(file)
        except:
            #traceback.print_exc()
            pass
        #sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', buffering=1)
    #count += 1
    """
   
    """
    if os.path.getsize("output.txt") <= 5:
        sys.stdout.buffer.write(file)
        print(os.path.getsize("output.txt"))
        #print(os.stat("output_100B").st_size)
        pass
    else:
        #print("larger")
        pass
    """
    """
    with open("time.txt", "a") as f:
        #f.write("Receive: " + time.ctime() + "\n")
        f.write("Receive: " + str(datetime.now()) + "\n")
    """
#print(time.time())
#print(datetime.now())
#mqttBroker ="mqtt.eclipseprojects.io"
mqttBroker = "raspberrypi"
#mqttBroker = "34.68.50.129"
#mqttBroker = "127.0.0.1"
#mqttBroker = "10.2.1.255"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)
#print(type(os.stat("output.txt").st_size))
#print(os.stat("output.txt").st_size)
#print(os.path.getsize("output.txt"))
outputFile = "output.txt"

#while True:
while count < 10000:
    client.loop_start()
    client.subscribe("TEMPERATURE", qos=2)
    client.on_message=on_message

    #time.sleep(2)
    client.loop_stop()