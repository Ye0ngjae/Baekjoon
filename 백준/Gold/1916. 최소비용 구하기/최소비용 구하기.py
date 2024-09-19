import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [False] * (N+1)
distance = [99999999] * (N+1)

queue = PriorityQueue()
A = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    u,v,w = map(int, sys.stdin.readline().split())

    A[u].append((v,w))

start, end = map(int, sys.stdin.readline().split())

queue.put((0,start))
distance[start] = 0

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
    
print(distance[end])