import sys
input = sys.stdin.readline

n,m,k=map(int, input().split())  # 수의개수, 변경횟수, 구간곱출력횟수
treeHeight=0  # 트리높이
length=n  # 리프노드개수
MOD=1000000007

while length!=0:
    length//=2
    treeHeight+=1

treeSize=pow(2,treeHeight+1)  # 트리길이
leftStartIdx=treeSize//2-1  # 리프노드 전 인덱스
tree = [1]*(treeSize+1)  # 인덱스 트리 저장 리스트

# 데이터를 리프노드에 저장
for i in range(leftStartIdx+1, leftStartIdx+n+1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(idx):
    while idx!=1:  # 인덱스가 루트노드가 아닐때까지
        tree[idx//2]=tree[idx]*tree[idx//2]%MOD
        idx-=1

setTree(treeSize-1)  # 2ᵏ-1부터 2까지
# print(tree)

# 값 변경 함수
def changeVal(idx, val):
    tree[idx]=val
    while idx>1:
        idx=idx//2
        tree[idx]=tree[idx*2]%MOD*tree[idx*2+1]%MOD

# 구간곱 출력 함수
def getMul(sIdx, eIdx):
    mul = 1
    while sIdx <= eIdx:
        if sIdx%2==1:  # 선택 : 부모노드 대상범위 제거, 독립노드
            mul=mul*tree[sIdx]%MOD
            sIdx+=1
        sIdx=sIdx//2
        if eIdx%2==0:  # 선택 : 부모노드 대상범위 제거, 독립노드
            mul=mul*tree[eIdx]%MOD
            eIdx-=1
        eIdx=eIdx//2
    return mul

for _ in range(m+k):
    q,s,e = map(int, input().split())
    if q == 1:  # 변경
        changeVal(leftStartIdx+s, e)
    elif q == 2:  # 출력
        b = leftStartIdx+s
        c = leftStartIdx+e
        print(getMul(b, c))
