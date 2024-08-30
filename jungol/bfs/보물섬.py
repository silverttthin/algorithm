import sys
sys.stdin = open('input.txt','r')

from collections import deque

r,c = map(int,input().split())

matrix = [list(input()) for _ in range(r)]

dx = [1,0,0,-1]
dy = [0,-1,1,0]
ans = 0

def check(i,j,visited):
    if 0<=i<r and 0<=j<c and matrix[i][j] == 'L' and visited[i][j] == 0: return True
    else: return False

def bfs(i,j):
    q = deque([[i,j,0]])
    visited = [[0] * c for _ in range(r)]

    visited[i][j] = 1
    max_depth = 0

    while q:
        [y,x,depth] = q.popleft()
        max_depth = visited[y][x]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if check(ny,nx, visited):
                q.append([ny,nx,depth + 1])
                visited[ny][nx] = visited[y][x] + 1
    return max_depth - 1


for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'L':
            ans = max(ans, bfs(i,j))
            
print(ans)