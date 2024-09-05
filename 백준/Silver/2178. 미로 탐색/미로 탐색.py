import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

find_x = [0,0,-1,1]
find_y = [1,-1,0,0]

#상하좌우

count = 0

miro = []
visit = [[False] * M for _ in range(N)]

for i in range(N):
    miro.append(list(map(int, list(sys.stdin.readline().rstrip()))))

def BFS(i,j):
    global count 

    que = deque()
    que.append((i,j))

    visit[i][j] = True

    while que:
        now = que.popleft()

        for k in range(4):
            x = now[0] + find_x[k]
            y = now[1] + find_y[k]
            
            if x >= 0 and y >= 0 and x < N and y < M:
                if miro[x][y] != 0 and not visit[x][y]:
                    visit[x][y] = True
                    miro[x][y] = miro[now[0]][now[1]] + 1
                    que.append((x,y))

BFS(0,0)
print(miro[N-1][M-1])