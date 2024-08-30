import sys;sys.stdin = open('input.txt','r')

n = int(input())

# Greedy 풀이
# cnt = 0
# while n>=0: 
#     # 의외로 역으로 3만큼 감쇄하다 5배수일 때 걷어내도 됨
#     if n % 5 == 0:
#         cnt += n//5
#         print(cnt)
#         break
#     cnt+=1
#     n -= 3
# else: print(-1)


# DP 풀이 : dp[n] = 1 + min(dp[n-3], dp[n-5])
dp = [-1] * (n+1)
if n>=3:
    dp[3] = 1
if n>=5 :
    dp[5] = 1

for i in range(6, n+1):
    if dp[i-3]<0 and dp[i-5]<0: # 7처럼 만들수 없는 경우
        dp[i] = -1
    
    elif dp[i-3]>0 and dp[i-5]>0: # 15 = 5*2+5 = 3*4+3
        dp[i] = 1 + min(dp[i-3], dp[i-5])
    
    else: # 둘중 하나가 -1이면 무조건 다른거 고르기
        dp[i] = 1 + max(dp[i-3], dp[i-5])

print(dp[n])


