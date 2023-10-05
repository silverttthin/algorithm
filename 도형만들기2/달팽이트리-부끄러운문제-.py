import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
# if n ==1: # 밑의 조건문을 제대로 작성했다면 필요 없었을 구문
#     print(0)
#     exit()

lst = [[-1 for _ in range(2*n-1)] for _ in range(n)]
distance, noon = n-1, 0
a,b = 0, n-1

while distance >0:
    movement = 1
    while movement<=distance:
        if noon ==10: noon = 0
        lst[a][b] = noon
        noon += 1
        a+=1
        b-=1
        movement += 1
    
    movement = 1

    while movement<=distance:
        if noon ==10: noon = 0
        lst[a][b] = noon
        noon += 1
        b+=2
        movement += 1

    movement = 1

    while movement<=distance:
        if noon ==10: noon = 0
        lst[a][b] = noon
        noon += 1
        a-=1
        b-=1
        movement += 1

    distance-=3
    a+=2
    # b = n-1


if lst[a][b] == -1: # 왜 여기를 n%2==0으로 조건을 처리했을까..
    if noon ==10: noon = 0
    lst[a][b] = noon

for i in range(n):
    for j in range(2*n-1):
        elem = lst[i][j]
        if elem == -1 : print("", end=" ")
        else: print(elem, end="")
    print()






