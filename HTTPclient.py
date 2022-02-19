import requests
import time
import statistics
import sys

file_name = sys.argv[1]
num_transfers = int(sys.argv[2])

file_location = 'http://192.168.1.53:8000/' + file_name
transfer_times = []

for i in range(0, num_transfers):
    start = time.time()
    req = requests.get(file_location, timeout = 10)
    end = time.time()
    transfer_times.append(end-start)

avg = statistics.mean(transfer_times)
std_d = statistics.stdev(transfer_times)
content_length = len(req.content)
header_length = sys.getsizeof(req.headers)
data_overhead = (content_length + header_length) / content_length
kb = content_length / 1000
avg_kbps = kb / avg
std_kbps = avg_kbps - (kb / (std_d + avg))

print("kb num:" , kb)
print("Header " + str(req.headers))
#print("content " + str(req.content))
print("Average time in seconds: " , avg)
print("Standard deviation in seconds: " , std_d)
print("Size of header in bytes: " , header_length)
print("Size of content in bytes: " , content_length)
print("Size of data transferred divided by file size: " , data_overhead)
print("Average throughput in Kbps: " , avg_kbps)
print("Standard deviation of throughput in Kbps: " , std_kbps)
transfer_times.clear()