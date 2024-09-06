import sys
import heapq

N = int(sys.stdin.readline())

A = []

for i in range(N):
    heapq.heappush(A, int(sys.stdin.readline()))

i = 0
j = 0
sum = 0

while len(A) > 1:
    i = heapq.heappop(A)
    j = heapq.heappop(A)

    sum += (i+j)
    heapq.heappush(A, i+j)

print(sum)