import sys;sys.stdin=open('input.txt','r')

n = int(input())
stairs= [0]*(n+1)
for i in range(1, n+1):
    stairs[i] = int(input())
dp = [0] * (n+1) # ith 계단일때 가지는 최대값 저장
if n==1: 
    print(stairs[n])
    exit()
elif n==2:
    print(stairs[1]+stairs[2])
    exit()

# 1st,2nd는 base
dp[1] = stairs[1] 
dp[2] = stairs[1] + stairs[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    # ith계단은 i-2에서 두칸점프해 오거나 i-1에서 한칸 점프해 올 수 있다.
    # 3계단연속 불가조건 -> 후자는 무조건 두칸 점프가 추가로 수반된다.
print(dp[n])