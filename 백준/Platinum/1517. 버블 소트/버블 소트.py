import sys

count = 0

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

def merge_sort(start, end):
    global count, A
    
    if start < end:
        mid = (start + end) // 2
        
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        temp = []
        left, right = start, mid + 1

        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp.append(A[left])
                left += 1
            else:
                temp.append(A[right])
                right += 1
                count += (mid - left) + 1

        if left <= mid:
            temp = temp + A[left:mid + 1]

        if right <= end:
            temp = temp + A[right:end + 1]

        for i in range(len(temp)):
            A[start+i] = temp[i]
        


merge_sort(0, N-1)

print(count)