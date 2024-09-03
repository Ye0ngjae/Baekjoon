import sys
from collections import deque

N,L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

que = deque()
ans =[]

for i in range(N):
    while que and que[-1][0] > A[i]:
        que.pop()
    
    que.append((A[i],i))
    if que[0][1] <= i -L:
        que.popleft()
    ans.append(que[0][0])

for i in range(len(ans)):
    print(ans[i], end=' ')