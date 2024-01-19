import sys
input = sys.stdin.readline
k,n =map(int, input().split())
arr = [] #랜선의 길이
for _ in range(k):
  arr.append(int(input()))
start = 1
end =sum(arr)//n
while start<=end:
  mid = (start+end)//2
  cnt = [l//mid for l in arr]
  if sum(cnt)>=n:
    start = mid+1
  else:
    end = mid -1
print(end)