import sys

while(1):
    a,b = 0,0
    stack = []
    str = sys.stdin.readline().replace("\n","")

    if str == ".":
        break
    
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                a = 1
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                a = 1
                break
    if len(stack) == 0 and a == 0:
        print("yes")
    else:
        print("no")
    