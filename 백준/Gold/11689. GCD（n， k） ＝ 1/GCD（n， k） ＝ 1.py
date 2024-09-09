import sys
import math

N = int(sys.stdin.readline().rstrip())
index = N

for i in range(2, int(math.sqrt(N)+1)):
    if N % i == 0:
        index -= index/i

        while N % i == 0:
            N /= i

if N > 1:
    index -= index/N

print(int(index))