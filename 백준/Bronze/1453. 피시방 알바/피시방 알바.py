import sys

reduced_size = 0
N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))

unique_arr = list(set(arr))
reduced_size = len(arr) - len(unique_arr)
print(reduced_size)