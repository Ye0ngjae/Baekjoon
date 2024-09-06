import sys
import heapq

N = int(sys.stdin.readline())

A = []
B = []

sum = 0
one = 0
zero = 0

for i in range(N):
    temp = int(sys.stdin.readline())

    if temp > 1:
        heapq.heappush(A, -temp)
    elif temp == 1:
        one += 1
    else:
        heapq.heappush(B, temp)

while len(A) > 1:
    i = -heapq.heappop(A)
    j = -heapq.heappop(A)
    sum += (i*j)

if len(A) != 0:
    for i in range(len(A)):
        sum += -A[i]

while len(B) > 1:
    i = heapq.heappop(B)
    j = heapq.heappop(B)

    sum += (i*j)

if len(B) != 0:
    for i in range(len(B)):
        sum += B[i]

sum += one

print(sum)