import sys

N = int(sys.stdin.readline())

A = [0] * 1200000

for i in range(len(A)):
    A[i] = i

for i in range(2, len(A)):
    if A[i] != 0:
        for j in range(i+i, len(A), i):
            A[j] = 0

for i in range(2,1200000):
    if A[i] != 0 and A[i] >= N:
        st = str(A[i])
        st1 = ''.join(reversed(st))

        if st == st1:
            print(A[i])
            break