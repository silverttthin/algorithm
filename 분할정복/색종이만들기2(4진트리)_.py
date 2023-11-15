import sys
sys.stdin = open('input.txt','r')

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
ans = []

def divider(lst, n): # 입력받은 2중 리스트가 단색인지 체크하고 아니면 분할
    div1 = [lst[i][0:n//2] for i in range(n//2)]

    div2 = [lst[i][n//2 : n] for i in range(n//2)]

    div3 = [lst[i][0:n//2] for i in range(n//2, n)]

    div4 = [lst[i][n//2 : n] for i in range(n//2, n)]

    for i in range(n):
        for j in range(n):
            if lst[i][j] != lst[0][0] : 
                # 현재 색종이는 단색이 아니므로 분할을 해야함
                ans.append('X')
                divider(div1, n//2)
                divider(div2, n//2)
                divider(div3, n//2)
                divider(div4, n//2)
                return
    if lst[0][0] == 0 : ans.append(0)
    else : ans.append(1)
    

divider(lst, N)

ans = list(map(str,ans))
print(''.join(ans))
