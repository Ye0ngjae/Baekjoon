import sys

arr = []
count = 1
tmp = 0

T = int(sys.stdin.readline())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

tmp = arr[0][1]
for i in range(1,T):
    if tmp <= arr[i][0]:
        count += 1
        tmp = arr[i][1]
    else:
        continue

print(count)