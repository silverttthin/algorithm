import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10 ** 4)
# x,y까지 몇번만에 왔냐를 저장해 기준으로 삼아 백트래킹
# 왜냐하면 x,y지점 도착후 어떻게 움직일지와 몇번만에 왔는지는 독립이라서

n,m = map(int,input().split())
hr,hc,jr,jc = map(int,input().split())
hr -= 1
hc -= 1
jr -= 1
jc -= 1

board = [[99999 for _ in range(m)] for _ in range(n)]

col=[2,1,-2,-1,2,1,-2,-1]
row=[1,2,1,2,-1,-2,-1,-2]
ans = 99999 # 졸의 위치에 도달했을 때 movecnt따로 담아둘 변수
def dfs(r,c, movecnt):
    global ans

    board[r][c] = movecnt

    # 어떤 지점에 도달했는데 더 적게 도달했으면 업데이트
    # 0이라면 아직 도달해보지 않은 곳이므로 무조건 업데이트

    # 근데 이미 왔던 곳인데 더 적게 왔었다면 혹은 이동횟수가 ans를 초과했다면 탐색 불필요
    if movecnt > ans: 
        return

    if r == jr and c == jc : 
        if board[r][c] >= ans: return
        ans = movecnt
        return


    for i in range(8):
        # 말이 장외로 안넘어가고 동시에 다음에 이동할 위치의 movecnt가 현 movecnt+1보다 크면 탐색 불필요
        if (r+row[i] < n and r+row[i]>=0 ) and (c+col[i] < m and c+col[i]>=0) and board[r][c] + 1 <board[r+row[i]][c+col[i]]: 
            dfs(r+row[i], c+col[i], movecnt+1)

dfs(hr, hc, 0)

print(ans)