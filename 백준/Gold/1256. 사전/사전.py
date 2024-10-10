import sys

N, M, K = map(int, sys.stdin.readline().split())

DP = [[ 0 for j in range(202)] for i in range(202)]

for i in range(0, 201):
    for j in range(0, i+1):
        if j == 0 or j == i:
            DP[i][j] = 1
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j]
            if DP[i][j] > 1000000000:
                DP[i][j] = 1000000001

if DP[N+M][M] < K:
    print(-1)
else:
    while not (N==0 and M==0):
        if DP[N-1+M][M] >= K:
            print("a", end='')
            N -= 1
        else:
            print("z", end='')
            K -= DP[N-1+M][M]
            M -= 1