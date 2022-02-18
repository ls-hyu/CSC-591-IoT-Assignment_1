import math

experiment_file = str(sys.argv[1])

# 傳輸的檔案大小(kilobits)
kilo_bits = 0

if experiment_file == '100B':
    kilo_bits = 0.8
elif experiment_file == '10KB':
    kilo_bits = 80
elif experiment_file == '1MB':
    kilo_bits = 8000
elif experiment_file == '10MB':
    kilo_bits = 80000

start = open('start_time.txt', 'r')
end = open('end_time.txt', 'r')

intervals = []

def variance(data, ddof, mean):
    return sum((x - mean) ** 2 for x in data) / (len(data) - ddof)

def stdev(data, mean):
    var = variance(data, 0, mean)
    std_dev = math.sqrt(var)
    return std_dev

while True:
    # Get next line from file
    s_line = start.readline()
    e_line = end.readline()

    if s_line != '' or e_line != '':
        intervals.append(float(e_line) - float(s_line))
 
    # if line is empty
    # end of file is reached
    if not s_line:
        break
 
start.close()
end.close()

# 平均（每輪實驗）傳送需花幾秒
mean_of_each_experiment = sum(intervals) / len(intervals)
# 傳輸的檔案大小(kb) / 平均（每輪實驗）傳送需花幾秒
kilobits_per_sec = kilo_bits / mean_of_each_experiment

print(f"Kilo bits per second: {kilobits_per_sec}")
print(f"Standard deviation: {stdev(intervals, kilobits_per_sec)}")