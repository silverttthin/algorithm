import sys
sys.stdin = open('input.txt','r')

N = int(input())

arr = list(map(int,input().split()))
s= 0
ans = 0
for i, num in enumerate(arr):
    s += num
    if s<0:
        s=0
        continue

    else:
        ans = max(ans, s)

print(ans)
