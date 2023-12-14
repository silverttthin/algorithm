import sys
sys.setrecursionlimit(10000)

sys.stdin = open('input.txt','r')

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(i,j):
    global field
    
    field[i][j] = 0

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<n and 0<=ny<m and field[nx][ny] == 1:
            dfs(nx,ny)
    return


T = int(input())
for _ in range(T):
    m, n, cabbage = map(int,input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    earthwarm_cnt = 0

    for _ in range(cabbage):
        x,y = map(int,input().split())
        field[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                dfs(i,j)
                earthwarm_cnt +=1
    
    print(earthwarm_cnt)




