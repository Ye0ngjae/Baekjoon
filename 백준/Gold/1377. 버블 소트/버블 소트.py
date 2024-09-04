import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append((int(sys.stdin.readline()), i))

MAX = 0

sorted_A = sorted(A)
for i in range(N):
    if MAX < sorted_A[i][1] - i:
        MAX = sorted_A[i][1] - i

print(MAX+1)