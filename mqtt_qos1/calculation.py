import math

start = open('start_time.txt', 'r')
end = open('end_time.txt', 'r')

intervals = []

def variance(data, ddof, total):
    mean = total / len(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - ddof)

def stdev(data, total):
    var = variance(data, 0, total)
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

# 傳輸的檔案大小(kb)
file_size_kb = 1000

# 傳輸的檔案大小(kb) / 平均（每輪實驗）傳送需花幾秒
kb_per_sec = file_size_kb / (sum(intervals) / len(intervals))

print(f"kb per second: {kb_per_sec}")
print(f"Standard deviation: {stdev(intervals, kb_per_sec)}")