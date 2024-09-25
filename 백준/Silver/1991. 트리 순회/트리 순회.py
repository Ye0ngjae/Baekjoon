import sys

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    a,b,c = map(str, sys.stdin.readline().split())
    tree[a] = [b,c]

def check(tmp):
    if tmp == '.':
        return True
    else:
        return False

def preorder(num):
    if check(num):
        return

    print(num, end='')
    preorder(tree[num][0])
    preorder(tree[num][1])

def inorder(num):
    if check(num):
        return
    
    inorder(tree[num][0])
    print(num, end='')
    inorder(tree[num][1])
    

def postodrder(num):
    if check(num):
        return
    
    postodrder(tree[num][0])
    postodrder(tree[num][1])
    print(num, end='')
    
    

preorder('A')
print()
inorder('A')
print()
postodrder('A')