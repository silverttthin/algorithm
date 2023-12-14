import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt','r')

n = int(input())
picture = [[c for c in input()] for _ in range(n)]
picture2 = [line[:] for line in picture]
for i in range(n):
    for j in range(n):
        if picture2[i][j] == 'G': picture2[i][j] = 'R'
dx = [-1,0,1,0]
dy = [0,1,0,-1]

area  = [0,0]

def dfs(i,j, matrix):
    color = matrix[i][j]
    matrix[i][j] = 0

    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]
        if 0<=nx<n and 0<=ny<n and matrix[ny][nx] == color:
            dfs(ny,nx,matrix)
    return


for i in range(n):
    for j in range(n):
        if picture[i][j] != 0:
            dfs(i,j, picture)
            area[0] += 1

for i in range(n):
    for j in range(n):
        if picture2[i][j] != 0:
            dfs(i,j, picture2)
            area[1] += 1

print(*area)