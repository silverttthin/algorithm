import sys;sys.stdin=open('input.txt','r')

a = '_'+input()
b = '_'+input()

R = len(a)-1
C = len(b)-1

dp = [[0] * (C+1) for _ in range(R+1)]
# dp[r][c]  = 각 문자열을 r,c 인덱스까지만 쓸때 LCS의 길이
# a[r] b[c]가 만약
# 같다면 max(dp[r-1][c-1]+1, dp[r-1][c], dp[r][c-1])
# 다르다면 max(dp[r-1][c], dp[r][c-1])

# abc bcd  -> abc vs bc or ab vs bcd

for i in range(1, R+1):
    for j in range(1, C+1):
        if a[i] == b[j]: 
            dp[i][j] = dp[i-1][j-1] +1
        
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

print(dp[R][C])