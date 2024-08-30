import sys
sys.setrecursionlimit(10**5)

sys.stdin = open('input.txt','r')

y,x = map(int, input().split())
icebergs = [list(map(int,input().split())) for _ in range(y)]
dx = [1,0,0,-1]
dy = [0,-1,1,0]

def dfs(i,j): 
    visited[i][j] = 1
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]

        if 0<=nx<x and 0<=ny<y and icebergs[ny][nx] !=0 and visited[ny][nx] == 0:
            dfs(ny,nx)

def mass_check(): # 빙산 몇 덩어리인지 체크
    cnt= 0
    for i in range(y):
        for j in range(x):
            if icebergs[i][j]!=0 and visited[i][j] ==0 :
                dfs(i,j)
                cnt+=1
    return cnt

def melting(icebergs):  # 나중에 수정
    melting_amount_matrix = [[0]*x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if icebergs[i][j] > 0 :
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]

                    if icebergs[i][j] >0 and icebergs[ny][nx] == 0:
                        # icebergs[i][j] -= 1 일캐하면 녹는 양 계산이 이미 줄어든 이웃칸에 영향받아 독립이 아니게됨
                        melting_amount_matrix[i][j] += 1
                    
    else:
        for i in range(y):
            for j in range(x):
                tmp = icebergs[i][j] - melting_amount_matrix[i][j]
                if tmp < 0 : 
                    icebergs[i][j] = 0
                else :
                    icebergs[i][j]= tmp


year = 0
visited = [[0]*(x) for _ in range(y)]
default_mass = mass_check()

while 1:
    melting(icebergs)
    visited = [[0]*(x) for _ in range(y)]
    now_mass = mass_check()
    if now_mass == 0 :
        print(0)
        break
    year +=1
    if default_mass != now_mass :
        print(year)
        break
    




