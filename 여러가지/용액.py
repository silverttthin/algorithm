import sys
sys.stdin = open('input.txt','r')

n=int(input())
lst=list(map(int,input().split()))

l = 0
r = len(lst)-1

ans = 2500000000
w = [0,0]
while l<r:
    s=lst[l]+lst[r]
    if ans>abs(s):
        ans = abs(s)
        w = [lst[l],lst[r]]

    if s>0:
        r-=1
    elif s<0:
        l+=1
    else: break

print(w[0], w[1])
