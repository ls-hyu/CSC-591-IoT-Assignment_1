import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import sys

def on_message(client, userdata, message):
    print("!!!!!!!!!!!!!!!!!!!!!!!")
    #print("received message: " ,str(message.payload.decode("utf-8")))

#mqttBroker ="mqtt.eclipseprojects.io" 
#mqttBroker = "10.2.1.255"
#mqttBroker = "raspberrypi"
#mqttBroker = "34.68.50.129"
#mqttBroker = "34.68.50.129"
#mqttBroker = "10.0.2.15"
mqttBroker = "127.0.0.1"
#port = 1883

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 
#client.connect(mqttBroker, port)

while True:
    randNumber = uniform(20.0, 21.0)
    file = sys.stdin.buffer.read(1024*1024*1024)
    with open("time.txt", "a") as f:
        client.subscribe("#", qos=2)
        client.publish("TEMPERATURE", file, qos=2)
        print("SENT")
        #client.loop()
        client.loop_start()
        client.on_message = on_message
        client.loop_stop()
        f.write("Send: " + time.ctime() + "\n")

    time.sleep(5)