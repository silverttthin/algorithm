import sys
sys.stdin= open('input.txt', 'r')

n= int(input())

lst= [[-1 for _ in range(n+2)] for _ in range(n+2)]
for i in range(0, n+2):
    lst[0][i]= 0
    lst[i][0]= 0
    lst[i][n+1]= 0
    lst[n+1][i]= 0

r, c, num = 1, 1, 1

# 오른쪽 위로(-r +c)
# 왼쪽 아래로(+r -c)
# 오른쪽(불가능하면 아래)
# 아래(불가능하면 오른쪽)

# 불가능 조건 : 
while num <= n**2:
    while lst[r][c] == -1: # 좌하단
        lst[r][c]= num
        num+=1
        r+= 1
        c-= 1
    r-=1
    c+=1

    # 아래
    if lst[r+1][c] != 0: r+= 1
    else: c+=1

    while lst[r][c] == -1: # 우상단
        lst[r][c]= num
        num+=1
        r-= 1
        c+= 1
    r+= 1
    c-= 1

    # 오른쪽

    if lst[r][c+1] == -1: c+=1
    else: r+= 1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(lst[i][j], end=" ")
    print()

