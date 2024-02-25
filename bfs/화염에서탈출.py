# 두개의 요소가 동시에 움직일 때
# 미리 각각의 분포도 완성시키고 비교하기
# 이때 중간의 경로가 막히는 것도 고려하기(하단주석)

import sys
from collections import deque

r,c = map(int,input().split())
map_ = [list(input()) for _ in range(r)]

dx = [1,0,0,-1]
dy = [0,-1,1,0]

flame_map = [[1000000] * c for _ in range(r)]
human_map = [[1000000] * c for _ in range(r)]
flame_q = deque([])
def bfs():
    global flame_map, flame_q

    while flame_q:
        [y,x,depth] = flame_q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<c and 0<=ny<r and map_[ny][nx] == '.' and flame_map[ny][nx] > depth + 1:
                flame_q.append([ny,nx,depth + 1])
                flame_map[ny][nx] = depth + 1


def bfs2(i,j):
    global human_map
    q= deque([[i,j,0]])
    human_map[i][j]= 0

    while q:
        [y,x,depth] = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<c and 0<=ny<r and human_map[ny][nx] > depth + 1 and map_[ny][nx] != 'X' and flame_map[ny][nx] > depth + 1 :
                q.append([ny,nx,depth + 1])
                human_map[ny][nx] = depth + 1

for i in range(r):
    for j in range(c):
        if map_[i][j] == '*':
            flame_q.append([i,j,0])
            flame_map[i][j] = 0
        elif map_[i][j] == 'S':
            human_i,human_j = i, j
        elif map_[i][j] == 'D':
            D_i,D_j = i, j

bfs()
bfs2(human_i,  human_j)


if human_map[D_i][D_j] != 1000000:
    print(human_map[D_i][D_j])

else: print('impossible')

