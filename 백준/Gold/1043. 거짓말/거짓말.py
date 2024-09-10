import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    if x == parents[x]:
        return x
    
    return find(parents[x])
    
n,m = map(int,input().split())
parents = [i for i in range(n+1)]
_,*t = map(int,input().split())

for i in t:
    parents[i] = 0

partys = []
for _ in range(m):
    p,*q = map(int,input().split())
    partys.append(q)
    if p == 1:
        continue
    
    for i in range(p-1):
        union(q[i],q[i+1])

ans = 0
for party in partys:
    for i in party:
        if find(parents[i]) == 0:
            break
    else:
        ans+=1
print(ans)