import sys
from collections import deque

N = int(sys.stdin.readline().strip())

a = []

for i in range(N):
    input_data = sys.stdin.readline().strip().split()
    c = int(input_data[0])
    if len(input_data) > 1:
        num = int(input_data[1])
    
    if c == 1:
        a.append(num)
    elif c == 2:
        if not a:
            print(-1)
        else:
            print(a.pop())  
    elif c == 3:
        print(len(a))
    elif c == 4:
        if not a:
            print(1)
        else:
            print(0)
    elif c == 5:
        if not a:
            print(-1)
        else:
            print(a[-1])
              