import sys
sys.stdin = open("input.txt",'r')


n = int(input())
scores = [0] * (n+1)
for i in range(1, n+1):
    scores[i] = int(input())

# dp = [[0]*(n+1) for _ in range(2)]
# dp[0][1] = scores[1]
# for i in range(2, n+1):
#     dp[0][i] = max(dp[0][i-2] + scores[i], dp[1][i-2] + scores[i])
#     dp[1][i] = dp[0][i-1] + scores[i]
# print(max(dp[0][n], dp[1][n]))
# dp 0행은 i-2번째 계단에서 i번째 계단으로 한번에 두계단 오른 것이다.
# 한번에 두계단은 아무 조건없이 가능하므로 그냥 i-2에서 큰거 가져오면 된다.
# dp 1행은 i번째 계단으로 한번에 한계단 올라와 도착한 것이다.
# 3계단을 연속으로 걸을 수 없어 한번에 한계단은 2번오를 수 없다. 
# 따라서 한번에 한계단 올라오는 1행은 무조건 한번에 두계단에서 가져와야 한다.

# (더간단하게)
# i번째 계단에 올라오는 경우는 두가지이다.
    # 1. i-2번째 계단에서 두계단 건너뛰어 올라오면 dp[i] = dp[i-2] + scores[i]
    # 2. i-1번째 계단에서 한계단 건너뛰어 올라오는 경우
    # 이경우는 반드시 i-3번째 계단에서 두계단 건너뛰어 i-1로 온 경우이다.'

dp = [0] * (n+1)
dp[1] = scores[1]
dp[2] = dp[1] + scores[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

print(dp[n])
