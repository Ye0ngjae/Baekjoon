import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

start = max(A)
end = sum(A)


while start <= end:
    mid = (start + end) // 2

    class_sum = 0 
    count = 0 

    for i in range(N):
        if class_sum + A[i] > mid:
            count += 1
            class_sum = 0
        class_sum += A[i]

    if class_sum != 0:
        count += 1
    if count > M:
        start = mid + 1
    
    else:
        end = mid - 1

print(start)