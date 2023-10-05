import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

if m== 1:
    arr = [[0 for i in range(n+1)] for j in range(n)]
    arr[0][1] = 1
    for row in range(1, n):
        for col in range(1, row+2):
            arr[row][col] = arr[row-1][col-1] + arr[row-1][col]

    for row in arr:
        for elem in row[1:]:
            if elem ==0: print(" ", end=" ")
            else: print(elem, end=" ")
        print()

elif m== 3:
    arr = [[0 for i in range(n)] for j in range(n+1)]
    arr[n-1][n-1] = 1
    for col in range(n-2, -1, -1):
        for row in range(n-1, col-1,-1):
            arr[row][col]= arr[row][col+1] + arr[row+1][col+1]

    for row in arr:
        for elem in row:
            if elem ==0: print(" ", end=" ")
            else: print(elem, end=" ")
        print()


else:
    arr = [[0 for i in range(n+2)] for j in range(n+2)]

    # 종류 1을 뒤집은 꼴을 먼저 만들고 
    arr[n][1] = 1
    for i in range(n-1, 0, -1):
        for j in range(1, n-i+2):
            arr[i][j] = arr[i+1][j] + arr[i+1][j-1]
    # 위에서부터 앞의 공백을 만들며 출력
    for i in range(1, n+1):
        for j in range(1, i):
            print(' ', end='')
        for j in range(1, n-i+2):
            print(arr[i][j], end=' ')
        print()



