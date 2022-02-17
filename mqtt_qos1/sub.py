# python3.6

import random

from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "file_transfer"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
f_out = open("./sub/1MB","wb") #use a different filename

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_message(client, userdata, msg):
    f_out.write(msg.payload)
    

def run():
    client = connect_mqtt()
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    run()
    f_out.close()
