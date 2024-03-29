import sys

N = int(sys.stdin.readline().rstrip())

a = dict()

for i in range(N):
    M, P = map(str, sys.stdin.readline().split())

    if P == 'enter':
        a[M]=P
    else:
        del a[M]

temp = sorted(a.keys(),reverse=True)

for i in temp:
    print(i)    