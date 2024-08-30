import sys
from collections import deque

sys.stdin = open('input.txt','r')

r,c = map(int,input().split())
horse_r,horse_c,jol_r,jol_c = map(int,input().split())
visited = [[False] * (r+1) for _ in range(c+1)]

dx=[2,2,1,-1,-2,-2,1,-1]
dy=[1,-1,-2,-2,1,-1,2,2]

def bfs(horse_r,horse_c):
    q = deque([[horse_r, horse_c, 0]])
    visited[horse_r][horse_c] = True


    while q:
        y,x, movement = q.popleft()
        if (y,x) == (jol_r,jol_c):
            print(movement)
            return

        for i,j in zip(dy,dx):
            ny,nx = y + i, x + j
            if 0<nx<=c and 0<ny<=r and not visited[ny][nx]:
                q.append([ny,nx, movement+1])
                visited[ny][nx] = True

bfs(horse_r,horse_c)

