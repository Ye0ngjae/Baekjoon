import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

visited = [False] * (N+1)
tree = [[] for _ in range(N+1)]
result = [0] * (N+1)

for _ in range(1,N):
    A,B = map(int, sys.stdin.readline().split())

    tree[A].append(B)
    tree[B].append(A)

def DFS(num):
    visited[num] = True

    for i in tree[num]:
        if not visited[i]:
            result[i] = num
            DFS(i)

DFS(1)

for i in range(2,N+1):
    print(result[i])