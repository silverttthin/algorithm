import sys
sys.setrecursionlimit(100000)

sys.stdin = open('input.txt','r')


y,x = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(y)]
dx = [1,0,0,-1]
dy = [0,-1,1,0]

hour = 0

def air_changing(i,j): 
    visited[i][j] = 1

    if cheese[i][j] == 0: # 내부공기와 구분을 위해 외부 공기를 2로 바꿈
        cheese[i][j] = 2
    
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]

        if 0<=nx<x and 0<=ny<y and visited[ny][nx] == 0 and cheese[ny][nx] != 1:
            air_changing(ny,nx)

while 1:
    flag = 0 # 치즈가 다 녹았는지 확인 플래그
    for i in range(y):
        if flag == 1 : break
        for j in range(x):
            if cheese[i][j] == 1:
                flag = 1
                break

    if flag == 0 :
        print(hour)
        break

    visited = [[0] * x for _ in range(y)]
    air_changing(0,0)

    # 녹는 작업 구현
    # 1이면 주변에 '2'가 2개 이상이면 빈 테이플에 해당지점 값 -1 을 저장 (0 미만이면 그냥 0 저장)
    # 붙여넣기

    cheese_cpy = [line[:] for line in cheese]
    for i in range(y):
        for j in range(x):
            if cheese[i][j] == 1:
                air_cnt = 0
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]

                    if 0<=nx<x and 0<=ny<y and cheese[ny][nx] == 2:
                        air_cnt += 1
                    
                if air_cnt>=2 :
                    cheese_cpy[i][j] = cheese[i][j] - 1
    
    hour += 1
    cheese = cheese_cpy

                





