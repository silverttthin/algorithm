import sys
sys.setrecursionlimit(1000000000)

sys.stdin = open('input.txt','r')


y,x = map(int,input().split())
_map = [list(map(int,input().split())) for _ in range(y)]
case_map = [[-1 for _ in range(x)] for _ in range(y)]
case_map[y-1][x-1] = 1

dx=[1,0,0,-1]
dy=[0,1,-1,0]

def dfs(i,j): 
    if case_map[i][j] != -1:
        return case_map[i][j]
    
    case_map[i][j] = 0

    # i,j에서 출발해 도착점에 도달하는 경우의 수를 구하기
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]

        if 0<=nx<x and 0<=ny<y and _map[ny][nx] < _map[i][j]:
            case_map[i][j] += dfs(ny,nx)

    return case_map[i][j]

print(dfs(0,0))