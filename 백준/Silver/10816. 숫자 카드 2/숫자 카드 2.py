import sys
from collections import Counter

N = int(sys.stdin.readline())

arr1 = sys.stdin.readline().split()

T = int(sys.stdin.readline())

arr2 = sys.stdin.readline().split()

counter = Counter(arr1)

for i in range(T):
    print(counter[arr2[i]], end=' ')