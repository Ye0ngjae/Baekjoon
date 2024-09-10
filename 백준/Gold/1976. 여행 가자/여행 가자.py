import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parent = [0] + [i for i in range(1,N+1)]
city = [[0 for j in range(N+1)] for i in range(N+1)]
connected = False

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

for i in range(1, N+1):
    city[i] = list(map(int,sys.stdin.readline().split()))
    city[i].insert(0,0)

route = list(map(int, sys.stdin.readline().split()))
route.insert(0,0)

for i in range(1, N+1):
    for j in range(1, N+1):
        if city[i][j] == 1:
            union(i,j)

temp = find(route[1])

for i in range(2, len(route)):
    if temp != find(route[i]):
        print("NO")
        exit()

print("YES")