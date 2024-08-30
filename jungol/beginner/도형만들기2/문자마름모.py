import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

chars = [chr(i) for i in range(65, 91)]

arr = [[0 for _ in range(n*2-1)] for _ in range(n*2-1)]



distance = n-1 # 한사이클 끝나면 반드시 -1

# a++b-- => a++b++ => a--b++ => a--b--

x = 0
y = int((n*2-1)/2)

c_idx = 0

while distance >0:

    movement = 1
    while movement <= distance:
        if c_idx>=26 : c_idx = 0

        arr[x][y] = chars[c_idx]
        x+=1
        y-=1
        c_idx+=1
        movement += 1
    movement = 1

    while movement <= distance:
        if c_idx>=26 : c_idx = 0

        arr[x][y] = chars[c_idx]
        x+=1
        y+=1
        c_idx+=1
        movement += 1
    movement = 1
    

    while movement <= distance:
        if c_idx>=26 : c_idx = 0

        arr[x][y] = chars[c_idx]
        x-=1
        y+=1
        c_idx+=1
        movement += 1
    movement = 1

    while movement <= distance:
        if c_idx>=26 : c_idx = 0

        arr[x][y] = chars[c_idx]
        x-=1
        y-=1
        c_idx+=1
        movement += 1
    
    distance -= 1
    x+=1

if c_idx>=26 : c_idx = 0
arr[x][y] = chars[c_idx]

for i in range(n*2-1):
    for j in range(n*2-1):
        if arr[i][j] == 0:
            print(" ", end= " ")
        else : 
            print(arr[i][j], end=" ")
    print()
