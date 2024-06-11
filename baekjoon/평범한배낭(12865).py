import sys;sys.stdin=open('input.txt','r')

n, k = map(int, input().split())

# n은 물품수, k는 배낭최대무게
# dp[r][현재 순회 무게] = max(dp[r-1][현재순회무게], dp[r-1][i - w] + price])

dp = [[0] * (k+1) for _ in range(n+1)]

items = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
# 1 base index

for itemIdx in range(1, n+1):
    weight, price = items[itemIdx]
    for gram in range(1, k+1):
        if gram>=weight:
            dp[itemIdx][gram] = max(dp[itemIdx-1][gram],
                                price + dp[itemIdx-1][gram - weight])
        else:
            dp[itemIdx-1][gram]

print(max(dp[-1]))

