import sys

num = sys.stdin.readline()

num = list(num)

num.sort(reverse=True)

for i in num:
    print(i, end='')