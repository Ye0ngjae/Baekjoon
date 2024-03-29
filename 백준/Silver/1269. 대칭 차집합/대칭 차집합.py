import sys

N, M = map(int, sys.stdin.readline().split())

a = set()
b = set()

temp = sys.stdin.readline().split()
a.update(temp)


temp = sys.stdin.readline().split()
b.update(temp)

print(len(a-b)+len(b-a))

