import random
import asyncio
import sys
import time
from paho.mqtt import client as mqtt_client

experiment_file = str(sys.argv[1])
experiment_reps = int(sys.argv[2])

broker = 'localhost'
port = 1883
topic = "file_transfer"
client_id = f'python-mqtt-{random.randint(0, 100)}'
time_records = []
count = 0

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, message):
    global count
    time_records.append(time.time())
    count += 1
    print(count)
    if count == experiment_reps:
        record_time()
        
def record_time():
    f = open("end_time.txt", "a+")
    for t in time_records:
        f.write(str(t)+"\n")
    f.close()

def run():
    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    client.on_connect = on_connect
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    run()
