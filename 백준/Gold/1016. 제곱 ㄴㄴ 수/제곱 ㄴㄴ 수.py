import sys

MIN, MAX = map(int, sys.stdin.readline().split())

a = [i**2 for i in range(2,int(MAX**0.5)+1)]
A = [1] * (MAX-MIN+1)

for i in a:
    n = MIN//i*i
    while(n < MAX+1):
        if n - MIN >= 0:
            A[n-MIN] = 0
        n += i
print(sum(A))