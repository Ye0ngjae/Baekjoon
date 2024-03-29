import sys

N, M = map(int, sys.stdin.readline().split())

a = list()
count = 0

for i in range(N):
    a.append(sys.stdin.readline().rstrip())

for i in range(M):
    b = (sys.stdin.readline().rstrip())
    if b in a:
        count += 1

print(count)

