import sys
sys.stdin = open('input.txt','r')
from collections import deque

col,row = map(int,input().split())
m = [[int(c) for c in input().rstrip()] for _ in range(row)]

atk_c, atk_r = map(lambda x : x-1, map(int,input().split()))
visited = [[False] * col for _ in range(row)]


dx,dy = [-1,0,1,0],[0,-1,0,1]
def bfs():
    q = deque([[atk_r,atk_c,3]])
    visited[atk_r][atk_c] = True
    m[atk_r][atk_c] = 0

    while q:
        r,c,cnt = q.popleft()
        max_cnt = cnt

        for k in range(4):
            nx = c + dx[k]
            ny = r + dy[k]
            if 0<=nx<col and 0<=ny<row and m[ny][nx] == 1 and not visited[ny][nx]:
                q.append([ny,nx,cnt+1])
                visited[ny][nx] = True
                # m[ny][nx] = 0 
            
    return max_cnt

print(bfs())
print(([row.count(1) for row in m]))