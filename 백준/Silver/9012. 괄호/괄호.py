import sys

T = int(sys.stdin.readline())

for i in range(T):
    a = 0
    str = sys.stdin.readline().replace("\n","")

    for j in range(len(str)):
        if str[j] == '(':
            a += 1
        else:
            a -= 1

        if a < 0:
            print("NO")
            break

    if a > 0:
        print("NO")
    elif a == 0:
        print("YES")
            