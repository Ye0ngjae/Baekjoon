import sys

num = int(sys.stdin.readline().strip())

board = [[0 for _ in range(100)] for _ in range(100)]

for i in range(num):
    N, M = map(int, sys.stdin.readline().strip().split())

    for j in range(M, M+10):
        for k in range(N, N+10):
            board[j][k] = 1

result = 0
for i in range(100):
    result += board[i].count(1)
print(result)