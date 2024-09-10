import sys

n,m = map(int, sys.stdin.readline().split())

parent = [0] * (n+1)

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

def check(a,b):
    x = find(a)
    y = find(b)

    if x == y:
        return True
    else:
        return False
    

for i in range(1,n+1):
    parent[i] = i 

for _ in range(m):
    order, a,b = map(int, sys.stdin.readline().split())

    if order == 1:
        result = check(a,b)
        
        if result == True:
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)