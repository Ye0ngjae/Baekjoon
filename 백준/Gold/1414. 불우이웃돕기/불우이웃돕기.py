import sys

def find(x):

    if x!=disjoint[x]:
        disjoint[x]=find(disjoint[x])
    return disjoint[x]

def union(a,b):

    a=find(a)
    b=find(b)

    if a>b:
        disjoint[a]=b
    else:
        disjoint[b]=a

N=int(sys.stdin.readline())
Arr=[ list(sys.stdin.readline().rstrip()) for _ in range(N) ]
disjoint=[ _ for _ in range(N+1) ]

edge=[] ; total=0

for i in range(N):
    for j in range(N):

        if Arr[i][j]==0:
            edge.append((0,i+1,j+1))
        else:
            if ord('a')<=ord(Arr[i][j])<=ord('z'):

                edge.append((ord(Arr[i][j])-ord('a')+1 , i+1 , j+1))
                total+=ord(Arr[i][j])-ord('a')+1

            elif ord('A')<=ord(Arr[i][j])<=ord('Z'):

                edge.append((ord(Arr[i][j])-ord('A')+27 , i+1,j+1))
                total+=ord(Arr[i][j])-ord('A')+27

edge.sort(key=lambda x:x[0])

for value,x,y in edge:

    if value==0:
        continue

    if find(x)!=find(y):
        union(x,y)
        total-=value

check=set()
for i in range(1,N+1):
    if find(i) not in check:
        check.add(find(i))

if len(check)==1:
    print(total)
else:
    print(-1)