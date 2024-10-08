import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
Sum = sum(arr)

arr2 = [0] * 51

ans = 0

for i in range(0, N):
    if arr[i] >= K:
        arr2[i] = 1
        for k in range(0,K):
            arr2[i] = arr2[i] * (arr[i] - k) / (Sum -  k)
        ans += arr2[i]

print(ans)