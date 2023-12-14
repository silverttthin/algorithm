import sys
sys.setrecursionlimit(100000)

sys.stdin = open('input.txt','r')

y, x = map(int,input().split())
board = [[0 for _ in range(x)] for _ in range(y)]

dx = [1,0,0,-1]
dy = [0,-1,1,0]
for i in range(y):
    string = input()
    for j in range(x):
        board[i][j] = string[j]
check = [0 for i in range(26+1)]
ans = 1

check[ord(board[0][0])-ord('A')] = 1

def dfs(i,j,cnt):
    global ans
    ans = max(ans,cnt)
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]

        
        if 0<=nx<x and 0<=ny<y and board[ny][nx]:
            num = ord(board[ny][nx]) - ord('A')
            if check[num] != 1:
                check[num] = 1
                dfs(ny,nx,cnt+1)
                check[num] = 0

dfs(0,0,1)
print(ans)
