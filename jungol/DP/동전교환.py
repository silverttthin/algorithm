import sys
sys.stdin = open('input.txt','r')

n = int(input())
coin_units = list(map(int,input().split()))
w = int(input())

dp = [10000000000] * (w+1)
dp[0] = 0

for unit in coin_units:
    for i in range(unit, w+1):
        dp[i] = min(dp[i], 1 + dp[i-unit])

if dp[-1] == 10000000000:
    print('impossoble')
else:
    print(dp[-1])
