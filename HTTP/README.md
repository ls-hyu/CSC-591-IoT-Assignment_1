# HTTP

## Introduction
In this portion, we create a HTTP server on one PC and a HTTP client on another PC. The HTTP server will store 
files on its file system and the HTTP client will request them from the server. 

## Software Requirements
- `pip install python`
  - Requires python 3.7.4 or later
- `pip install requests`
  - Abstracted HTTP library that can be used to request and decode data from a HTTP server 
- HTTP module comes pre-installed with python 3.7.4 or later

### Deploying the server
On the first PC, a HTTP server was deployed on Port 8000 using the python cmd, “python –m http.server 8000”

### Run the client
On the second PC, run the HTTP client.
The HTTP client program accepts the following command line arguments:
1. file_name
2. num_transfers
For example, you use the following command to run the HTTP client to request the 100B file to be transferred 10,000 times:
- `python HTTPclient.py 100B 10000`

