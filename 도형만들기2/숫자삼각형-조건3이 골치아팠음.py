import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

if n%2==0 or n>100 or m<0 or m>3:
    print("INPUT ERROR!")
    exit()

if m ==1:
    arr = [[0 for _ in range(n)] for _ in range(n)]
    a,b = 0,0
    t = 1

    for row in range(n):
        for tmp in range(row+1):
            arr[row][tmp] = t
            t+=1
    
    for row in range(n):
        if row%2 == 1:
            arr[row][:] = arr[row][::-1]
    
    for row in arr:
        for num in row:
            if num != 0:
                print(num, end=" ")
        print()

elif m ==2: 
    width = n * 2 - 1
    arr = [[-1 for _ in range(width)] for _ in range(n)]

    for i in range(n):
        if i == 0 :
            arr[0][:] = [0] * width
        else:
            arr[i][i:width-i] = [i] * len(arr[i][i:width-i])
    
    for i in range(n):
        for j in range(width):
            if arr[i][j] == -1:
                print(" ", end=" ")
            else :
                print(arr[i][j], end=" ")
        print()

elif m ==3 : 
    arr = [[-1 for _ in range((n+1)//2)] for _ in range(n)]

    for i in range((n+1)//2): # 0 1 2
        if i == (n+1)//2 - 1:
            arr[i][i] = i+1
        else:
            for j in range(i,n-1-i + 1): # 0일 때 0~n-1, 1일 때 1~n-2...
                arr[j][i] = i+1
    
    for row in range(n):
        for col in range((n+1)//2):
            if arr[row][col] == -1:
                print("",end=" ")
            else:
                print(arr[row][col], end=" ")
        print()

        