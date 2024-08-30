import sys

sys.stdin = open('input.txt','r')

n = int(input())

chars = [chr(i) for i in range(65, 91)]

arr = [[0 for _ in range(n)] for _ in range(n)]

a = 0
c_idx= 0
col = -1
for i in range(n): # 대각선 반복문
    a = i
    col = -1
    while a<n:
        arr[a][col] = chars[c_idx] # a가 i를 따라가야함
        c_idx +=1
        a+=1
        col -= 1
        if c_idx >=26:
            c_idx = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0 :
            print(" ", end=" ")
        else : 
            print(arr[i][j], end=" ")
    print()




