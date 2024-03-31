import sys

N = int(sys.stdin.readline().rstrip())

i = 0

while N > i:
    N -= i
    i += 1
    

if i % 2 == 0:
    a = N
    b = i - N + 1

else:
    a = i - N + 1
    b = N

print(str(a)+'/'+str(b))
