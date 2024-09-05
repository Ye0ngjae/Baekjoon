import sys
sys.setrecursionlimit(100000)
N, M = map(int, sys.stdin.readline().split())


graph = [[] for i in range(N+1)]

visit = [False] * (N+1)
count = 0

def DFS(i):
    global graph, visit

    visit[i] = True

    for j in graph[i]:
        if not visit[j]:
            DFS(j)

for i in range(M):
    n1, n2 = map(int,sys.stdin.readline().split())

    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1,N+1): 
    if visit[i] == False:
        count += 1
        DFS(i)

print(count)