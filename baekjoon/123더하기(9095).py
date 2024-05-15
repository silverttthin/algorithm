import sys;sys.stdin=open('input.txt','r')

T= int(input())

dp = [1]* 11
dp[0] = 0
dp[1] = 1
dp[2] = 2 # 2, 1+1
dp[3] = 4 # 3, 2+1, 1+2, 1+1+1 
for i in range(4, 10+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    #i-1 +1, i-2 + 2, i-3 +3 가짓수와 같음
    #왜냐하면 합을 1,2,3의 합으로 나타내니

for _ in range(T):
    print(dp[int(input())])