import sys

#arr = list(sys.stdin.readline().rstrip())
arr = list(map(int,list(sys.stdin.readline().rstrip())))

N = len(arr)

for i in range(N):
    MAX = i

    for j in range(i,N):
        if arr[j] > arr[MAX]:
            MAX = j
    if arr[i] < arr[MAX]:    
        tmp = arr[i]
        arr[i] = arr[MAX]
        arr[MAX] = tmp

for i in range(N):
    print(arr[i], end='')