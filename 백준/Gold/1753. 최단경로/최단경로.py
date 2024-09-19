import sys
from queue import PriorityQueue

V,E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = 2147000000
visited = [False] * (V+1)
distance = [INF] * (V+1)

queue = PriorityQueue()
A = [[] for _ in range(V+1)]

for _ in range(1, E+1):
    u,v,w = map(int, sys.stdin.readline().split())

    A[u].append((v,w))

queue.put((0,K))
distance[K] = 0

while queue.qsize() > 0:
    now = queue.get()
    cv = now[1]
    if visited[cv]:
        continue
    visited[cv] = True

    for temp in A[cv]:
        next = temp[0]
        value = temp[1]

        if distance[next] > distance[cv] + value:
            distance[next] = distance[cv] + value

        queue.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")