import sys

N, M = map(int, sys.stdin.readline().split())
count = 0
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

for i in range(N, 0, -1):
    if M == 0:
        break
    if M >= arr[i-1]:
        count += M // arr[i-1]
        M = M % arr[i-1]
print(count)