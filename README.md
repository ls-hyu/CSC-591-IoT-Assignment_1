# CSC-591-IoT-Assignment_1
# MQTT QoS 2

Use MQTT protocol with quality of service of 2 to send files. The server would one file to the client. Both of the time of each packet sent and received would be wriiten in the time.txt.

## Instructions

You would need at least two devices to perform the task, one laptop as both client and server and one raspberry pi zero W as broker.

1. Use the following command to install the open-source broker Mosquitto on the raspberry pi:
```
sudo apt-get install mosquitto
```

> See if the broker is running:
```
sudo service mosquitto status
```
2. Use the following command to start the MQTT2_server.py:

```
python MQTT2_server.py < DataFiles/{FileName}
```
3. Use the following command to start the MQTT2_client.py:
```
python MQTT2_client.py > DataFiles/{OutputFileName}
```
> Change the number of the loop as needed.
4. See the timestamps of the packets sent and received in the time.txt.

## Additional files 

#### Throughput.py

Calculate the transmission time of the packets.
```
python Throughput.py
```
> change the last part of the function depending on the file size.
