import sys
sys.stdin = open('input.txt','r')

# Longest Increasing Subsequence 
# 가장 긴 부분수열 길이 찾기 by DP

# 가장 긴 부분수열을 유지한채 옮겨야 최소횟수
n= int(input())
arr = [int(input()) for _ in range(n)]

dp = [1] * (n+1)
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))