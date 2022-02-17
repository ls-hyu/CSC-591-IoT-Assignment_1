import random
import time
import sys

from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "file_transfer"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

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

def publish(client, byte_arr, qos = 1):
    result = client.publish(topic, byte_arr, qos)
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
    # for arr in [["1MB", 100], ["10KB", 1000], ["10MB", 10], ["100B", 10000]]:
    for arr in [["1MB", 2]]:
        byte_arr = get_byte_arr(arr[0])
        for i in range(arr[1]):
            publish(client, byte_arr, 1)

def run():
    client = connect_mqtt()
    client.loop_start()
    run_experiments(client)


if __name__ == '__main__':
    run()
