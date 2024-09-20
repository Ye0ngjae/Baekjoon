import sys

N, M = map(int, sys.stdin.readline().split())

INF = sys.maxsize
Min = INF
answer = -1

distance = [[INF for j in range(N+1)] for i in range(N+1)]

for i in range(N+1):
    distance[i][i] = 0

for i in range(M):
    A,B = map(int, sys.stdin.readline().split())

    distance[A][B] = 1
    distance[B][A] = 1

for k in range(1,N+1):
    for s in range(1,N+1):
        for e in range(1,N+1):
            distance[s][e] = min(distance[s][e], distance[s][k] + distance[k][e])

for i in range(1, N+1):
    sum = 0

    for j in range(1,N+1):
        sum += distance[i][j]
    
    if Min > sum:
        Min = sum
        answer = i

print(answer)