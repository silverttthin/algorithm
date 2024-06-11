n = int(input())

# 마지막 수와 길이를 기준으로 표를 구성했다

dp = [[0]*10 for _ in range(n)]

for i in range(n):
    dp[i][0] = 1
for i in range(10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(1, 9+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])

print(sum(dp[n-1])%10007)

