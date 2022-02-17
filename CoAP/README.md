# CoAP
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)

## Introduction

In this part, we are going to set up one computer as CoAP server and the other as CoAP client. The CoAP server will contain these files on its file system and the CoAP client will request them from the server. Moreover, we will caculate the transmitting time and compare the result with MQTT and HTTP. We will also caculate the total application layer data transferred from sender to receiver per file divided by the file size to measure the overhead. The comparison will record in `Results File.xlsx`.

## Setup

The below instructions can be followed in order to set-up at your end in a span of few minutes!

1. First of all, you need a `python3` and `pip3` in you PC

2. Clone the repository to your local system.

3. Start a terminal session in the CoAP directory. Run the following command to install the aiocoap library:
```
  pip3 install aiocoap
```
4. Run the coap-server.py in terminal.

5. Repeat the 1~3 instructions on another PC or a virtual machine.

6. Run the coap-client.py in terminal.

## CoAP Client
Files will transmit from server to client and save in `/CoAPdata/` folder in the client PC. Moreover, the file `/CoAPdata/time.xlsx` will record the time that sending each file cost. Modify the variables in `coap-client.py` to transmit different file for different times.

#### Variables in coap-client.py
filename => Which file we are going to transmit

columns => Store at which column in time.xlsx (fiename : columns = 100B : 1, 10KB : 2, 1MB : 3, 10MB : 4)

times => transmit the file for how many times (filename : times = 100B : 10000, 10KB : 1000, 1MB : 100, 10MB : 10)

firstRow => which row the data will store in time.xlsx (filename : firstRow =  100B : A1, 10KB : B1, 1MB : C1, 10MB : D1)



