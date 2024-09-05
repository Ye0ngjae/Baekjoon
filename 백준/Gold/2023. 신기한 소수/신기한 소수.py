import sys

def prime(n):
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
        
N = int(sys.stdin.readline())

def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(10):
            temp=num*10+i
            
            if prime(temp):
                DFS(temp)

DFS(2)
DFS(3)
DFS(5)
DFS(7)