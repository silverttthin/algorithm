import sys
sys.setrecursionlimit(500000)

sys.stdin = open('input.txt','r')
n = int(input())


forest = [list(map(int,input().split())) for _ in range(n)]
table = [[0]*n for _ in range(n)] # 어떤 칸에서 최대 이동가능한 칸수 저장
dx=[1,0,0,-1]
dy=[0,1,-1,0]

def dfs(i, j): 
    if table[i][j] != 0: return table[i][j] + 1

    flag = 0
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]
        
        if 0<=nx<n and 0<=ny<n and forest[ny][nx] > forest[i][j]:
            flag = 1
            table[i][j] = max(table[i][j], dfs(ny,nx))
        
    if flag == 0:
        table[i][j]= 1
        return 2
    
    return table[i][j] + 1

ans = -1
for i in range(n):
    for j in range(n):
        dfs(i,j)
        ans = max(ans, table[i][j])

print(ans)


