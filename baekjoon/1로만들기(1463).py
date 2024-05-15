import sys;sys.stdin=open('input.txt','r')

n= int(input())

dp = [0]*(n+1) # n에서 1을 만들기 위한 최소연산개수
if n>=2:
    dp[2] = 1 # 2는 1을 빼기만 하면 1이 된다
if n>=3:
    dp[3] = 1 # 3은 3으로 나누기만하면 1이 된다

for i in range(4, n+1):
    tmp = []
    if i %2 ==0:
        tmp.append(dp[i//2])
    if i%3 ==0:
        tmp.append(dp[i//3])
    
    tmp.append(dp[i-1])

    dp[i] = 1 + min(tmp)

print(dp[n])