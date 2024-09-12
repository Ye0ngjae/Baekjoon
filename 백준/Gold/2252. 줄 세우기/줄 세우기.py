import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
Arr = [[] for _ in range(N+1)]
entry = [0] * (N+1)

for i in range(M):
    A,B = map(int, sys.stdin.readline().split())
    Arr[A].append(B)
    entry[B] += 1

que = deque()

for i in range(1, N+1):
    if entry[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    print(now, end=' ')
    
    for i in Arr[now]:
        entry[i] -= 1
        
        if entry[i] == 0:
            que.append(i)
