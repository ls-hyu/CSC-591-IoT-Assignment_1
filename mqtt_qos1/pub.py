import random
import time
import sys
from paho.mqtt import client as mqtt_client

experiment_file = str(sys.argv[1])
experiment_reps = int(sys.argv[2])

broker = 'localhost'
port = 1883
topic = "file_transfer"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
time_records = []

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, payload, qos = 1):
    result = client.publish(topic, payload, qos)
    status = result[0]
    if status == 0:
        print(f"Send to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def get_byte_arr(f):
    with open(f, 'rb') as f_read:
        foo = f_read.read()
        f_read.close()
        byte_arr = bytes(foo)
        return byte_arr

def run_experiments(client):
    byte_arr = get_byte_arr(experiment_file)
    for i in range(experiment_reps):
        time_records.append(time.time())
        publish(client, byte_arr, 1)
        time.sleep(0.5)

def record_time():
    f = open("start_time.txt", "a+")
    for t in time_records:
        f.write(str(t)+"\n")
    f.close()

def run():
    client = connect_mqtt()
    client.loop_start()
    run_experiments(client)
    record_time()

if __name__ == '__main__':
    run()
