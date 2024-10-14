import sys

K, L = map(int, sys.stdin.readline().split())

a = {} 

for i in range(L):
    temp = sys.stdin.readline().rstrip()

    a[temp] = i

result = sorted(a.items(), key = lambda x:x[1])

if ( K > len(result)):
    K = len(result)

for i in range(K):
    print(result[i][0])