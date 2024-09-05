import sys
from collections import deque

N = int(sys.stdin.readline())

A = [[] for i in range(N+1)]

distance = [0] * (N+1)
visit = [False] * (N+1)

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))

    index = temp[0]
    for i in range(1,len(temp)-2,2):
        
        info = tuple([temp[i],temp[i+1]])
        A[index].append(info)

def BFS(i):
    global visit 

    que = deque()

    que.append(i)
    visit[i] = True 
    

    while que:
        now = que.popleft()

        for j in A[now]:
            if not visit[j[0]]:
                visit[j[0]] = True
                que.append(j[0])
                distance[j[0]] = distance[now] + j[1]

MAX = 1
BFS(MAX)
for i in range(1,N+1):
    if distance[MAX] < distance[i]:
        MAX = i

distance = [0] * (N+1)
visit = [False] * (N+1)
BFS(MAX)
print(max(distance))