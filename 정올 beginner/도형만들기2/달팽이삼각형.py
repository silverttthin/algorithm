import sys

sys.stdin = open('input.txt', 'r')
n = int(input())

lst = [[-1 for _ in range(n)] for _ in range(n)]

a, b = 0, 0
distance = n-1
num = 0
while distance > 0:
    movement = 1

    while movement <= distance:
        if num == 10: num = 0
        lst[a][b] = num
        num += 1
        a+=1
        b+=1
        movement+=1

    movement = 1
    while movement <= distance:
        if num == 10: num = 0
        lst[a][b] = num
        num += 1
        b-=1
        movement+=1


    movement = 1
    while movement <= distance:
        if num == 10: num = 0
        lst[a][b] = num
        num += 1
        a-=1
        movement+=1


    distance -= 3
    a+=2
    b+=1

if lst[a][b] == -1:
    if num == 10: num = 0
    lst[a][b] = num



for i in range(n):
    for j in range(n):
        if lst[i][j] != -1:
            print(lst[i][j], end=" ")
        else:
            print("", end=" ")
    print()