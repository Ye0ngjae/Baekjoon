import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
visit = [False] * (N+1)

arrive = False

def DFS(x,visited,cnt):

    global arrive

    if cnt == 4:
        arrive = True
        return

    visited[x] = True

    for i in graph[x]:
        if not visited[i]:

            DFS(i,visited,cnt+1)

    visited[x] = False

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    DFS(i,visit,0)
    if arrive:
        print(1)
        exit()

print(0)