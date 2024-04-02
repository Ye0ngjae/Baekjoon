import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
result = [sum(arr[:K])]

for i in range(N-K):
    result.append(result[i] + arr[i+K] - arr[i])

print(max(result))