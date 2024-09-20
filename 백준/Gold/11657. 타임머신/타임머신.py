import sys

INF = sys.maxsize

N, M = map(int, sys.stdin.readline().split())

city = []
distance = [INF] * (N+1)
isNegative = False

for _ in range(1,M+1):
    A,B,C = map(int, sys.stdin.readline().split())
    city.append((A,B,C))

distance[1] = 0

for i in range(N-1):
    for start, end, value in city:
        if distance[start] != INF and distance[end] > distance[start] + value:
            distance[end] = distance[start] + value

for start, end, value in city:
    if distance[start] != INF and distance[end] > distance[start] + value:
        isNegative = True

if not isNegative:
    for i in range(2, N+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)