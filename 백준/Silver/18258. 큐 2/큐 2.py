import sys
from collections import deque

arr = deque()

N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().split()

    a = command[0]
    if len(command) > 1:
        b = int(command[1])

    if a == "push":
        arr.append(b)
    elif a == "pop":
        if not arr:
            print(-1)
        else:
            print(arr.popleft())
    elif a == "size":
        print(len(arr))
    elif a == "empty":
        if not arr:
            print(1)
        else:
            print(0)
    elif a == "front":
        if not arr:
            print(-1)
        else:
            print(arr[0])
    elif a == "back":
        if not arr:
            print(-1)
        else:
            print(arr[-1])