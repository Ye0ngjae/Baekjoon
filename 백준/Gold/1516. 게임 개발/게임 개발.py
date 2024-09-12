import sys
from collections import deque

N = int(sys.stdin.readline())
A = [[] for _ in range(N+1)]
answer = [0] * (N+1)
time = [0] * (N+1)
entry = [0] * (N+1)
que = deque()

for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    time[i] = temp[0]

    for j in range(1,len(temp[1:-1])+1):
        A[temp[j]].append(i)
        entry[i] += 1

for i in range(1, N+1):
    if entry[i] == 0:
        que.append(i)

while que:
    now = que.popleft()

    for i in A[now]:
        entry[i] -= 1

        answer[i] = max(answer[i], time[now] + answer[now])
        
        if entry[i] == 0:
            que.append(i)

for i in range(1,N+1):
    print(answer[i] + time[i])