import sys
from collections import deque

sys.stdin = open('input.txt','r')

d = [(-1,0),(0,-1),(1,0),(0,1)]
hd = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
    (1, -2), (2, -1), (2, 1), (1, 2)]

def bfs():
    q = deque([[0,0,0]])
    while q:
        r,c,k = q.popleft()
        if r == h-1 and c == w-1: return visited[r][c][k] - 1 #
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0<=nr<h and 0<=nc<w and not visited[nr][nc][k] and m[nr][nc] != 1:
                q.append([nr,nc,k])
                visited[nr][nc][k] = visited[r][c][k] + 1
        if k < K:
            for idx in range(8):
                nr = r + hd[idx][0]
                nc = c + hd[idx][1]
                if 0<=nr<h and 0<=nc<w and not visited[nr][nc][k+1] and m[nr][nc] != 1:
                    q.append([nr,nc,k+1])
                    visited[nr][nc][k+1] = visited[r][c][k] + 1
    return -1


K=int(input())
w,h = map(int,input().split())
m = [list(map(int, input().split())) for _ in range(h)]

visited = [[[0] * (K+1) for _ in range(w)] for _ in range(h)]

visited[0][0][0] = 1

print(bfs())