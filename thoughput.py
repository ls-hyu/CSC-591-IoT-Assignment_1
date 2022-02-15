from datetime import datetime
import statistics as stat
import numpy as np
import pandas as pd

f = open("time_10MB.txt", "r")
lines = f.readlines()

count = 0
trans_time = []

for line in lines:
    timestamp = line.split(" ")[2][:-2]
    if line[0] == "R":
        receive_time = datetime.strptime(timestamp, "%H:%M:%S.%f")
        diff = receive_time - send_time
        trans_time.append(diff)
        print(diff)
        count += 1
    if line[0] == "S":
        send_time = datetime.strptime(timestamp, "%H:%M:%S.%f")

print(count)
trans_time = pd.DataFrame(trans_time)
print(trans_time)
#print(stat.stdev(trans_time[3]))
time_std = trans_time.std()
print(time_std)
time_mean = trans_time.mean()
print(time_mean)

#print(100/1024/(time_std / np.timedelta64(1, 's')))
#print(100/1024/(time_mean / np.timedelta64(1, 's')))
#print(10/(time_std / np.timedelta64(1, 's')))
#print(10/(time_mean / np.timedelta64(1, 's')))
#print(1024/(time_std / np.timedelta64(1, 's')))
#print(1024/(time_mean / np.timedelta64(1, 's')))
print(10320162/1024/(time_std / np.timedelta64(1, 's')))
print(10320162/1024/(time_mean / np.timedelta64(1, 's')))