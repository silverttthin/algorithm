import sys
sys.stdin = open('input.txt','r')

n, w = map(int,input().split()) # 각각 보석개수, 최대무게
jewels = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (w+1) for _ in range(n+1)]

for i in range(1, n +1): 
    weight, price = jewels[i-1]
    for j in range(1, w +1):
        if weight>j : 
            dp[i][j] = dp[i-1][j] # 지금 보석으로 j그램 불가하면 그냥 위에꺼 가져옴
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + price)
    # i번째 물건을 넣으려 할때 i-1번째 물건까지로 
print(max(dp[n]))

# dp = [-1] * (w+1)
# dp[0] = 0
# for weight, price in jewels:
#     for i in range(w, weight-1, -1):
#         if dp[i-weight] != -1:
#             dp[i] = max(dp[i], dp[i-weight] + price)

# print(max(dp))

# 개수가 한정됐을 땐 뒤에서부터 dp 돌기