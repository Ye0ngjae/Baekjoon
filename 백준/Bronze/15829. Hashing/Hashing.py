from sys import stdin

n = int(stdin.readline()) 
str_ = list(stdin.readline()) 
res = 0 

for i in range(n):
    res += ((ord(str_[i]) - 96) * (31 ** i))

print(res % 1234567891)