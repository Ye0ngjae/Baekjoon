import sys

arr1 = []
arr2 = []

N = int(input())
arr1 = set(sys.stdin.readline().split())

M = int(input())
arr2 = list(sys.stdin.readline().split())

for i in range(M):
    if arr2[i] in arr1:
        print(1)
    else:
        print(0)