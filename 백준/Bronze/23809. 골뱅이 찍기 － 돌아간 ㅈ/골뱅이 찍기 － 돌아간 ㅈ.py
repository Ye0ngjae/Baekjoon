import sys

T = int(sys.stdin.readline())

for _ in range(T):
    print('@' * T + ' ' * (T * 3) + '@' * T)

for _ in range(T):
    print('@' * T + ' ' * (T * 2) + '@' * T)

for _ in range(T):
    print('@' * T + '@' * T + '@' * T)

for _ in range(T):
    print('@' * T + ' ' * (T * 2) + '@' * T)

for _ in range(T):
    print('@' * T + ' ' * (T * 3) + '@' * T)
