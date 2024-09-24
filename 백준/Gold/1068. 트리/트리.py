import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
answer = 0

visited = [False] * (N+1)
tree = [[] for _ in range(N)]

Arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if Arr[i] != -1:
        tree[i].append(Arr[i])
        tree[Arr[i]].append(i)
    else:
        root = i

deleteNode = int(sys.stdin.readline())

def DFS(num):
    global answer
    visited[num] = True
    nowNode = 0
    for i in tree[num]:
        if not visited[i] and i != deleteNode:
            nowNode += 1
            DFS(i)
    if nowNode == 0:
        answer += 1



if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)