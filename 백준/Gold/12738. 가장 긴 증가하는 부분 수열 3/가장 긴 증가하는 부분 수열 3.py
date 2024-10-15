import sys

N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]

A1 = [A[0]]

def binary_search(e):
    start = 0
    end = len(A1) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if A1[mid] == e:
            return mid
        elif A1[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

for item in A:
    if A1[-1] < item:
        A1.append(item)
    else:
        idx = binary_search(item)
        A1[idx] = item

print(len(A1))