import sys
import math

T = int(sys.stdin.readline().strip())

for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    print(min(a, min(b, c)))
