import sys

arr = []

N = int(sys.stdin.readline())

for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    arr.append([a,b])

arr.sort()

for i in range(N):
    print(arr[i][0], arr[i][1])
