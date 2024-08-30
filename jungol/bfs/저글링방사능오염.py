import sys
from collections import deque

sys.stdin = open('input.txt','r')

# x,y기준으로 퍼져나가는 양상이여야 하는데
# dfs를 쓰면 이를 무시하고 이곳저곳 퍼져나감

row,col = map(int,input().split())
jeousagi = [list(map(int,input().strip())) for _ in range(col)]
x,y = map(int,input().split())


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    max_time = -1
    q = deque([[y,x]])
    jeousagi[y][x] = 3

    while q:
        i, j = q.popleft()
        max_time=max(max_time, jeousagi[i][j])
        
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]

            if 0<=nx<row and 0<=ny<col and jeousagi[ny][nx] == 1:
                q.append([ny,nx])
                jeousagi[ny][nx] = jeousagi[i][j]+1
    
    cnt = 0
    for i in range(col):
        for j in range(row):
            if jeousagi[i][j] == 1: cnt += 1

    print(max_time)
    print(cnt)

bfs(y-1,x-1)


