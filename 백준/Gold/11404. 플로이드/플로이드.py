import sys

INF = sys.maxsize
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

distance = [[INF for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    distance[i][i] = 0

for i in range(1, M+1):
    A,B,C = map(int, sys.stdin.readline().split())
    
    if distance[A][B] > C:
        distance[A][B] = C

for k in range(N+1):
    for s in range(N+1):
        for e in range(N+1):
            distance[s][e] = min(distance[s][e], distance[s][k] + distance[k][e])

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()

