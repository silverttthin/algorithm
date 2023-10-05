import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

arr = [[0 for i in range(n+2)] for j in range(n+2)]

row, col = 1, n//2 +1

for i in range(1, n**2 +1):
    arr[row][col]= i
    if i % n == 0:
        row+=1
    else:
        row-= 1
        col-= 1

    if row == 0:
        row = n
    elif col == 0:
        col= n
    
for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=" ")
    print()