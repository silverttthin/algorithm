import sys
sys.stdin = open('input.txt','r')

n=int(input())
_map = [[int(c) for c in input()] for _ in range(n)]
inspect_check = [[0 for i in range(n)] for i in range(n)]
lst = []
# 체크배열을 통해 이미 검사한 자리면 리턴한다
# 처음 검사한 1이면 인덱스 내부에서 상하좌우로 이동해 추가적인 1을 검색
def dfs(i, j):
    global cnt
    
    inspect_check[i][j] = 1
    cnt+=1
    # if 0<=i-1<n and inspect_check[i-1][j] !=1 and _map[i-1][j]==1 : 
    #     dfs(i-1,j)
    # if 0<=j-1<n and inspect_check[i][j-1] !=1 and _map[i][j-1]==1 : 
    #     dfs(i,j-1)
    # if 0<=j+1<n and inspect_check[i][j+1] !=1 and _map[i][j+1]==1 : 
    #     dfs(i,j+1)
    # if 0<=i+1<n and inspect_check[i+1][j] !=1 and _map[i+1][j]==1 : 
    #     dfs(i+1,j)
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<n and 0<=ny<n and inspect_check[nx][ny] !=1 and _map[nx][ny] == 1:
            dfs(nx,ny)
    return


for i in range(n):
    for j in range(n):
        if _map[i][j] == 1 and inspect_check[i][j]!=1: # 검사했던 1인지까지 봐야 cnt 중복체크 방지
            cnt=0
            dfs(i,j)
            lst.append(cnt)

print(len(lst))
lst.sort()
for i in lst:
    print(i)