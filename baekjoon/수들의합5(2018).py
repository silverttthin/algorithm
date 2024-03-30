# https://www.acmicpc.net/problem/1789

n = int(input())

l,r = 1,1
cnt = 0

while l<=r and r<=n:
    if l == r:
        s = l
    
    if s>n:
        s= s-l
        l+=1
    elif s<n:
        r+=1
        s= s+r
    else:
        cnt+=1
        r+=1
        s= s+r


print(cnt)