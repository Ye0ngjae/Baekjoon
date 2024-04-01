import sys
from collections import deque

arr = deque()

N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().split()

    try:
        a = command[0]
        b = int(command[1])
    except IndexError:
        a = command[0]

    if a == "1":
        arr.appendleft(b)

    elif a == "2":
        arr.append(b)

    elif a == "3":
        if not arr:
            print(-1)
        else:
            print(arr.popleft())

    elif a == "4":
        if not arr:
            print(-1)
        else:
            print(arr.pop())

    elif a == "5":
        print(len(arr))

    elif a == "6":
        if not arr:
            print(1)
        else:
            print(0)

    elif a == "7":
        if not arr:
            print(-1)
        else:
            print(arr[0])

    elif a == "8":
        if not arr:
            print(-1)
        else:
            print(arr[-1])