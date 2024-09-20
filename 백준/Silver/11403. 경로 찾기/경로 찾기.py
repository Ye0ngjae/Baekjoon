import sys

N = int(sys.stdin.readline())

distance = [[0] for i in range(N+1)] * (N+1)

for i in range(N):
    distance[i] = list(map(int, sys.stdin.readline().split()))


for k in range(N):
    for s in range(N):
        for e in range(N):
            if distance[s][k] == 1 and distance[k][e] == 1:
                distance[s][e] = 1

for i in range(N):
    for j in range(N):
        print(distance[i][j], end=' ')
    print()