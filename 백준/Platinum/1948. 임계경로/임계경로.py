import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

A = [[] for _ in range(n+1)]
reverse_A = [[] for _ in range(n+1)]
entry = [0] * (m+2)
count = 0

for _ in range(1, m+1):
    a,b,c = map(int, sys.stdin.readline().split())

    A[a].append((b,c))
    reverse_A[b].append((a,c))
    entry[b] += 1

start_city, end_city = map(int, sys.stdin.readline().split())

que = deque()
answer = [0] * (n+1)

que.append(start_city)

while que:
    now = que.popleft()

    for i in A[now]:
        entry[i[0]] -= 1

        answer[i[0]] = max(answer[i[0]], answer[now] + i[1])

        if entry[i[0]] == 0:
            que.append(i[0])

que.clear()

visit = [False] * (n+1)
visit[end_city] = True

que.append(end_city)

while que:
    now = que.popleft()

    for i in reverse_A[now]:
        if answer[i[0]] + i[1] == answer[now]:
            count += 1

            if not visit[i[0]]:
                visit[i[0]] = True
                que.append(i[0])

print(answer[end_city])
print(count)