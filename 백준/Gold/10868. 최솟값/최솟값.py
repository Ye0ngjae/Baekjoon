import sys
import math

N, M = map(int, sys.stdin.readline().split())

treeHeight = 0
tree_length = N

while tree_length != 0:
    tree_length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 -1
tree = [sys.maxsize] * (treeSize + 1)

for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(sys.stdin.readline())

def setTree(i):
    while i != 1:
        if tree[i // 2] > tree[i]:
            tree[i//2] = tree[i]
        i -= 1

setTree(treeSize - 1)

def getMin(start, end):
    Min = sys.maxsize
    while start <= end:
        if start % 2 == 1:
            Min = min(Min, tree[start])
            start += 1
        if end % 2 == 0:
            Min = min(Min, tree[end])
            end -= 1
        start = start // 2
        end = end // 2
    return Min

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    start = start + leftNodeStartIndex
    end = end + leftNodeStartIndex
    print(getMin(start, end))