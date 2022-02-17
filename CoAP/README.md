# CoAP
=========
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)

## Setup
-----

The below instructions can be followed in order to set-up at your end in a span of few minutes!

1. First of all, you need a python3 in you PC

2. Clone the repository to your local system.

3. Start a terminal session in the CoAP directory. Run the following command to install the required dependencies:
```
  pip install aiocoap
```
4. Run the coap-server.py in terminal.

5. Repeat the 1~3 instructions on another PC or a virtual machine and run coap-client.py in terminal.

## How it works
--------------

Files will transmit from server to client and save in `/CoAPdata/` folder in the client PC. Moreover, the file `/CoAPdata/time.xlsx` will record the time that each file cost. 
Modify the variables in coap-client.py to transmit different file for different times.

filename => Which file we are going to transmit

columns => Store at which column in time.xlsx

times => transmit the file for how many times

first row => which row the data will store in time.xlsx (columns:firstROw =  1:A1, 2:B1, 3:C1, 4:D1)



