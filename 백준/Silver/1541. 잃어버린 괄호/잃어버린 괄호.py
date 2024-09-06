import sys

math = list(map(str, sys.stdin.readline().rstrip().split('-')))

sum = 0


for i in range(len(math)):
    temp = 0 
    plus = str(math[i]).split('+')

    for j in range(len(plus)):
        temp += int(plus[j])

    if i == 0:
        sum += temp
    else:
        sum -= temp

print(sum)