import sys

N = int(sys.stdin.readline())
DP = [[0 for j in range(11)] for i in range(N+1)]

for i in range(1,10):
    DP[1][i] = 1

for i in range(2,N+1):
    DP[i][0] = DP[i-1][1]
    DP[i][9] = DP[i-1][8]

    for j in range(1,9):
        DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % 1000000000

sum = 0

for i in range(10):
    sum = (sum + DP[N][i]) % 1000000000

print(sum)