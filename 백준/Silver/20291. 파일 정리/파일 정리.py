import sys

N = int(sys.stdin.readline())

arr = {}

for i in range(N):
    a = sys.stdin.readline().strip().split('.')[1]
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1
    
for i in sorted(arr.keys()):
    print(i, arr[i])