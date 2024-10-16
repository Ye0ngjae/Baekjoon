import sys

N = int(sys.stdin.readline())
A = [0] + [*map(int, sys.stdin.readline().split())]

index = 0
maxLength = 1
B = [0] * 1000001
D = [0] * 1000001
ans = [0] * 1000001
B[maxLength] = A[1]
D[1] = 1

def binarySearch(start, end, now):
    while start < end:
        mid = (start+end) // 2
        if B[mid] < now:
            start = mid + 1
        else:
            end = mid
    return end

for i in range(2, N+1):
    if B[maxLength] < A[i]:
        maxLength += 1
        B[maxLength] = A[i]
        D[i] = maxLength
    else:
        index = binarySearch(1,maxLength, A[i])
        B[index] = A[i]
        D[i] = index

print(maxLength)
index = maxLength
x = B[maxLength] + 1

for i in range(N, 0, -1):
    if D[i] == index:
        ans[index] = A[i]
        index -= 1

for i in range(1, maxLength + 1):
    print(ans[i], end=' ')