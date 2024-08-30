t = int(input()) # 지폐금액
k = int(input()) # 동전 가짓수
coins = [list(map(int,input().split())) for _ in range(k)]

dp = [0]*(t+1) # dp[n] = n원을 만드는 동전의 경우의 수
dp[0] = 1 

# coin을 써서 money원을 cnt이하의 i개로 지불가능?
# O(k*t*cnt)
for coin, cnt in coins:
    for money in range(t, 0, -1):
        for i in range(1, cnt+1): 
            if money - coin*i < 0: 
            # w원이 i개 쓸때부터 음수면 i+1..개는 당연히 볼필요도없음
                break
            dp[money] += dp[money - i*coin]
                # money - coin *i 라는 부분문제값 사용되고있음
print(dp[t])

