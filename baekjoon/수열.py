import sys
sys.stdin = open("input.txt",'r')

n,k = map(int,input().split())
lst = list(map(int,input().split()))

s=0
for i in range(k):
    s += lst[i]
ans = s

for i in range(k, n):
    s = s - lst[i-k] + lst[i]
    ans = max(ans, s)

print(ans)