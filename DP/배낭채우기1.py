import sys
sys.stdin = open('input.txt','r')

n, max_weight = map(int,input().split())

jewels = []
for _ in range(n):
    w, p = map(int,input().split())
    jewels.append([w,p])

weight_dp = [0] * (max_weight+1)

for weight, price in jewels:
    for i in range(weight, max_weight+1):
        weight_dp[i] = max(weight_dp[i], weight_dp[i-weight] + price)

print(max(weight_dp))
