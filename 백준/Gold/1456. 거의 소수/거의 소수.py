import sys
import math

MAX = 10000000

A, B = map(int, sys.stdin.readline().split())

count = 0
AB = [0] * MAX

for i in range(len(AB)):
    AB[i] = i

for i in range(2,int(math.sqrt(len(AB)))):
    if AB[i] != 0:
        for j in range(i+i, len(AB), i):
            AB[j] = 0

for i in range(2, MAX):
    if AB[i] != 0:
        temp = AB[i]

        while AB[i] <= B/temp:
            if AB[i] >= A/temp:
                count += 1
            temp = temp * AB[i]

print(count)