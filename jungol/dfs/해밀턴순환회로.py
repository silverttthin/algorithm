import sys
sys.stdin = open('input.txt','r')

n = int(input())

costs = [list(map(int,input().split())) for _ in range(n)]
ans = 999999999

check = [0 for i in range(n+1)]
check[0], check[1] = 1, 1 # 1은 지나쳤다는 플래그

# 모든 정점을 한번씩만 가야 최소비용
def dfs(now_city, expense):
    global check
    global ans

    if expense >=ans : return

    if check[:] == [1] * (n+1): 
        if costs[now_city-1][0] != 0 and expense + costs[now_city-1][0] < ans: 
            ans =  expense + costs[now_city-1][0]



    for i in range(2, n+1):
        if check[i] != 1 and costs[now_city-1][i-1] != 0: 
            check[i] = 1
            
            dfs(i, expense + costs[now_city-1][i-1])
            check[i] = 0

dfs(1, 0)
print(ans)