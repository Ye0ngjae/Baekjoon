import hashlib

s = input()
s = hashlib.sha1(s.encode())
print(s.hexdigest())