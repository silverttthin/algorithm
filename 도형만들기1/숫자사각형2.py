import sys

sys.stdin = open('input.txt','r')

a, b = map(int, input().split())

arr = [[0 for _ in range(b)] for _ in range(a)]

k = 1
for i in range(a):
    for j in range(b):
        arr[i][j] = k
        k+=1

for row in range(a):
    if row%2 == 1:
        arr[row][:] = arr[row][::-1]

for row in arr:
    for num in row:
        print(num, end=" ")
    print()


