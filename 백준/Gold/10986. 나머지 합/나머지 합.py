import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

b = []

result = 0

for i in range(N):
    if i == 0 :
        b.append(arr[i])
    else:
        b.append(b[i-1] + arr[i])

for i in range(N):
    b[i] = b[i] % M

result += b.count(0)

c = Counter(b)

for key, value in c.items():
    result += value * (value-1) // 2

print(result)