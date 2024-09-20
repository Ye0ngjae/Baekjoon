import sys


N, start, end, M = map(int, sys.stdin.readline().split())
INF = sys.maxsize
arr = []
maxMoney = [-INF] * (N)

for _ in range(M):
    A,B,C = map(int, sys.stdin.readline().split())
    arr.append((A,B,C))

benefit = list(map(int, sys.stdin.readline().split()))

maxMoney[start] = benefit[start]

for i in range(N + 101):
    for s,e,v in arr:
        if maxMoney[s] == -1* sys.maxsize:
            continue
        elif maxMoney[s] == sys.maxsize:
            maxMoney[e] = sys.maxsize
        elif maxMoney[s] - v + benefit[e] > maxMoney[e]:
            maxMoney[e] = maxMoney[s] -v + benefit[e]
            if i >= N - 1:
                maxMoney[e] = sys.maxsize
          
if maxMoney[end] == -sys.maxsize:
    print("gg")
elif maxMoney[end] == sys.maxsize:
    print("Gee")
else:
    print(maxMoney[end])