arr = []
stack = []
str = []
temp = True

N = int(input())

for i in range(N):
    arr.append(int(input()))

j = 1

for i in range(N):
    num = arr[i]

    while j <= num:
        stack.append(j)
        str.append('+')
        j += 1

    if stack[-1] == num:
        stack.pop()
        str.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in str:
        print(i)