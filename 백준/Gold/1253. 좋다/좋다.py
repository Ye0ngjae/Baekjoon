import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

A.sort()

start = 0
end = 0
count = 0

for i in range(N):
    K = A[i]
    start = 0
    end = N-1

    while(start < end):
        if(A[start] + A[end] == K):
            if(start != i and end != i):
                count += 1
                break
            elif start == i:
                start += 1
            else:
                end -= 1
        elif(A[start] + A[end] < K):
            start += 1
        else:
            end -= 1
             
print(count)