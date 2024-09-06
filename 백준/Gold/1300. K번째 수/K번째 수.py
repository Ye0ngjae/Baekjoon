import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start = 0
end = K
result = 0

while start <= end:
    mid = (start+end) // 2
    
    count = 0

    for i in range(1,N+1):
        count += min((mid//i),N)

    if count < K:
        start = mid + 1
    
    else:
        result = mid
        end = mid - 1

print(result)