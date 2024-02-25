import sys
sys.stdin = open('input.txt','r')

from collections import deque
c,r = map(int,input().split())
tomatos = [list(map(int,input().split())) for _ in range(r)]

# 1은 익은 토마토, 0은 안익은, -1은 빈칸
# 1은 여러개일 수도 있음
# 1은 1일이 지나면 인접 칸을 1로 만듬
    # 인접 칸은 1일수도 0일수도 -1일수도 있으니 각각 처리

dx = [1,0,0,-1]
dy = [0,1,-1,0]
q = deque([])

def bfs():
    global tomatos

    while q:
        i,j, cnt = q.popleft()
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]

            if 0<=nx<c and 0<=ny<r:
                if tomatos[ny][nx] == 0:
                    q.append([ny,nx,cnt+1])
                    tomatos[ny][nx] = tomatos[i][j] + 1

for i in range(r):
    for j in range(c):
        if tomatos[i][j] == 1:
            q.append([i,j,0])

bfs()


ans = -1
for i in range(r):
    for j in range(c):
        if tomatos[i][j] == 0 :
            print(-1)
            exit()

        elif tomatos[i][j] >= 1:
            ans = max(ans, tomatos[i][j])

print(ans-1)
