import sys
sys.stdin = open('input.txt','r')

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

blue, white = 0, 0

def divider(lst, n): # 입력받은 2중 리스트가 단색인지 체크하고 아니면 분할
    global blue, white
    div1 = [lst[i][0:n//2] for i in range(n//2)]

    div2 = [lst[i][n//2 : n] for i in range(n//2)]

    div3 = [lst[i][0:n//2] for i in range(n//2, n)]

    div4 = [lst[i][n//2 : n] for i in range(n//2, n)]

    for i in range(n):
        for j in range(n):
            if lst[i][j] != lst[0][0] : 
                # 현재 색종이는 단색이 아니므로 분할을 해야함
                divider(div1, n//2)
                divider(div2, n//2)
                divider(div3, n//2)
                divider(div4, n//2)
                return
    if lst[0][0] == 0 : white += 1
    else : blue += 1
    

divider(lst, N)

print(white)
print(blue)
