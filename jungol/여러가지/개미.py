import sys
sys.stdin = open('input.txt','r')

ans = [0,0]
w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

a = (p + t) // w
x = (p+t) % w
if a %2 == 0:
    ans[0] = x
else:
    ans[0] = w-x

b = (q+ t)//h
y = (q+ t)%h
if b%2 == 0:
    ans[1] = y
else:
    ans[1] = h - y

print(*ans)