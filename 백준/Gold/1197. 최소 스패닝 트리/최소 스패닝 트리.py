import sys
from queue import PriorityQueue

V, E  = map(int, sys.stdin.readline().split())

parent = [0] * (V+1)
queue = PriorityQueue()

for i in range(V+1):
    parent[i] = i

for _ in range(1,E+1):
    A,B,C = map(int, sys.stdin.readline().split())

    queue.put((C,A,B))

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])

    return parent[x]


def union(a,b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = parent[x]

edge_count = 0
result = 0

while edge_count < (V-1):
    C,A,B = queue.get()

    if find(A) != find(B):
        union(A,B)
        result += C
        edge_count += 1

print(result)