import sys

sys.stdin = open('input.txt','r')

n = int(input())

chars = [chr(i) for i in range(65, 91)]
t = 0

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        arr[j][i] = chars[t]
        t+=1
        if t >= 26:
            t = 0
        
        

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()