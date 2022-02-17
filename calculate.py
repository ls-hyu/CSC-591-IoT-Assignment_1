import os

count = 0
with open("time.txt", "r") as f:
    for line in f.readlines():
        if line[0] == "R":
            count += 1

print(count)