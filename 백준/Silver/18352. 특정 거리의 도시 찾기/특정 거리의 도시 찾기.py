import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

answer = []
Arr = [[] for _ in range(N+1)]
visit  = [-1] * (N+1)

for i in range(M):
    A,B = map(int, sys.stdin.readline().split())
    Arr[A].append(B)

def BFS(v):
    que = deque()
    que.append(v)
    visit[v] += 1
    
    while que:
        now = que.popleft()
        for i in Arr[now]:
            if visit[i] == -1:
                visit[i] = visit[now] + 1
                que.append(i)

BFS(X)

for i in  range(N+1):
    if visit[i] == K:
        answer.append(i)


answer.sort()

if not answer:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])