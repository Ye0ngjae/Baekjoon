import sys
from heapq import heappush, heappop

INF = sys.maxsize

n, m, k = map(int, sys.stdin.readline().split())
A =[[] for _ in range(n + 1)]
distance = [[INF] * k for _ in range(n + 1)]
heap = []

def dijkstra(start):
    heappush(heap, [0, start])
    distance[start][0] = 0
    while heap:
        w, n = heappop(heap)
        for n_n, wei in A[n]:
            n_w = wei + w     
            if n_w < distance[n_n][k-1]:
                distance[n_n][k-1] = n_w
                distance[n_n].sort()
                heappush(heap, [n_w, n_n])

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    A[a].append([b, c])

dijkstra(1)

for i in range(1, n + 1):
    if distance[i][k-1] == INF:
        print(-1)
    else:
        print(distance[i][k-1])