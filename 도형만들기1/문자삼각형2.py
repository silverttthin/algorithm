import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

if 1<=n<=100 and n%2 == 1:
    chars = [chr(i) for i in range(65, 91)]

    col = (n+1)//2

    arr = [[0 for _ in range(col)] for _ in range(n)]
    c_idx = 0
    
    distance = 1
    for i in range(col-1, -1, -1): # n = 13 -> i = 
        movement = 1
        start_x, start_y = i, i

        while movement<= distance:
            if c_idx>=26: c_idx = 0
            arr[start_x][start_y] = chars[c_idx]
            start_x += 1
            movement += 1
            c_idx += 1

        distance += 2
        
        
    



    for i in range(n):
        for j in range(col):
            if arr[i][j] == 0 :
                print(" ", end=" ")
            else : 
                print(arr[i][j], end=" ")
        print()

else:
    print("INPUT ERROR")
