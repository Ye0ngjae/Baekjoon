import sys

N,M = map(int, sys.stdin.readline().split())

arr = [[0] * (N+1)]

for i in range(N):
    arr.append([0] + list(map(int, sys.stdin.readline().split())))

sarr = [[0] * (N+1) for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        sarr[i][j] = sarr[i][j-1] + sarr[i-1][j] - sarr[i-1][j-1] + arr[i][j]

for i in range(M):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    print(sarr[x2][y2] - sarr[x1-1][y2] - sarr[x2][y1-1] + sarr[x1-1][y1-1])
   
