import sys

N = int(sys.stdin.readline())

count = 0
sum = 0
start = 0
end = 0

while end != N:
    if sum == N:
        count += 1
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end
    
count += 1 

print(count)