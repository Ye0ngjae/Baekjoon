import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
tmp = []
ans = [-1] * N

for i in range(N):
    
    while tmp and A[tmp[-1]] < A[i]:
        ans[tmp.pop()] = A[i]
    
    tmp.append(i)

for i in range(N):
    print(ans[i], end=' ')

