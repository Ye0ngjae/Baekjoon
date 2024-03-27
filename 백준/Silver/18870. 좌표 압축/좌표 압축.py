import sys

N = int(sys.stdin.readline().strip())

a = list(map(int, sys.stdin.readline().strip().split()))

mid = sorted(a)[len(a)//2]

b = sorted(set(a))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

for num in a:
    index = binary_search(b, num)
    print(index, end=' ')
