import sys

N = int(sys.stdin.readline())

DP = [[0] * 2 for _ in range(N+1)]
DP[1][0] = 0
DP[1][1] = 1

for i in range(2,N+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0]

print(DP[N][0] + DP[N][1])