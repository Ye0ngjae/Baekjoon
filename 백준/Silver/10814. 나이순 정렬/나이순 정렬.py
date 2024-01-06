n = int(input())

arr = []

for i in range(n):
    a,b = input().split()
    arr.append((int(a),b))

arr.sort(key=lambda x: x[0])

for i in range(n):
    print(arr[i][0], arr[i][1])
