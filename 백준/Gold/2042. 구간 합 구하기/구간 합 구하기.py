import sys

N, M, K = map(int, sys.stdin.readline().split())

treeHeight = 0
length = N
while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex =treeSize // 2 -1
tree = [0] * (treeSize + 1)

for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(sys.stdin.readline())

def setTree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

setTree(treeSize - 1)

def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

def getSum(s,e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

for _ in range(M + K):
    question, s, e = map(int, sys.stdin.readline().split())

    if question == 1:
        changeVal(leftNodeStartIndex+s,e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s,e))