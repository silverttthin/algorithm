import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
distance = n-1
a,b,k= 0, n-1, 1


while k <= n**2:
    if distance == 0:
        arr[a][b] = k
        break

    movement = 1

    while movement <= distance:
        arr[a][b] = k
        k += 1
        b -= 1
        movement += 1
    movement = 1
    
    while movement <= distance:
        arr[a][b] = k
        k += 1
        a += 1
        movement += 1
    movement = 1
    
    while movement <= distance:
        arr[a][b] = k
        k += 1
        b += 1
        movement += 1
    movement = 1
    
    while movement <= distance:
        arr[a][b] = k
        k += 1
        a -= 1
        movement += 1
    
    a += 1
    b -= 1
    distance -= 2




for row in arr:
    for num in row:
        print(num, end=" ")
    print()