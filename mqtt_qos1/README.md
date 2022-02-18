# MQTT QOS1
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)

## Software Requirements

- Install Mosquitto as broker, .
    - Use brew if you are using mac. `brew install mosquitto`
    - See this tutorial if you are using Linux or Windows. http://www.steves-internet-guide.com/install-mosquitto-linux/

- Install Paho
    - `pip install paho-mqtt`


## Experiment Set Up

The below instructions can be followed in order to set-up at your end in a span of few minutes!

1. Make sure you have `python3` and `pip3` in your computers.

2. On first computer, run `brew services start mosquitto` to start a broker.

3. On the second computer, run `python3 sub.py file_name transfer_reps` (e.g. python3 sub.py 1MB 100)

4. On the third computer, run `python3 pub.py file_name transfer_reps` (e.g. python3 pub.py 1MB 100)

5. After complete the experiments, put `start_time.txt` and `end_time.txt` to the same directory where calculation.py is.

6. Run `python calculation.py` to get the average and standard deviation of throughput.

