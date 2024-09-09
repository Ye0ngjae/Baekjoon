import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
answer = [0] * (N+1)
Arr = [[] for _ in range(N+1)]

for i in range(M):
    A,B = map(int, sys.stdin.readline().split())

    Arr[A].append(B)

def BFS(v):
    que = deque()
    que.append(v)
    visit[v] = True

    while que:
        now = que.popleft()

        for i in Arr[now]:
            if not visit[i]:
                visit[i] = True
                answer[i] += 1
                que.append(i)

for i in range(1, N+1):
    visit = [False] * (N+1)
    BFS(i)

maxValue = max(answer)

for i in range(1,N+1):
    if answer[i] == maxValue:
        print(i, end=' ')