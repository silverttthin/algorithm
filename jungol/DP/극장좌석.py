import sys
sys.stdin = open('input.txt','r')
n = int(input())
m = int(input())
if n == m:
    print(1)
    exit()
# 1
# 12 21
# 123 213, 132
# 1234 2134 1324, 1243 2143
# 12345 21345 13245 12435 21435, 12354 21354 13254

# 맨뒤가 안바뀌면 그냥 f(n-1)과 완전 동일
# 맨뒤가 바뀌면 뒤에서 두자리가 차감되므로 f(n-2)와 완전 동일
# f(n) = f(n-1) + f(n-2) 
dp = [-1] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 40+1):
    dp[i] = dp[i-1] + dp[i-2]

lst = [0] * (n+1)
for _ in range(m):
    lst[int(input())] = 1

ans = 1
cnt = 0
for i in range(1, n+1):
    if lst[i] == 1:
        ans *= dp[cnt]
        cnt = 0
    else:
        cnt+= 1
if lst[-1] == 1:
    print(ans)
else:
    print(ans*dp[cnt])


