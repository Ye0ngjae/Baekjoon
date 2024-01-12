import sys

stack = []

N = int(input())

for i in range(N):
    command = sys.stdin.readline().split()
    try:
        a = command[0]
        b = int(command[1])
    except IndexError:
        a = command[0]

    if a == "push":
        stack.append(b)
    elif a == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif a == "size":
        print(len(stack))
    elif a == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif a == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

