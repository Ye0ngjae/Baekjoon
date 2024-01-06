import math

n = int(input())

a = str(math.factorial(n))

sum = 0 

for i in range(len(a)-1, -1, -1):
    if(a[i] == '0'):
        sum += 1
    else:
        break

print(sum)