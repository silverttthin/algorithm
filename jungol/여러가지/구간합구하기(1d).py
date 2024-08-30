import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = list(map(int,input().split()))

for i in range(1, n):
    arr[i] += arr[i-1]

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    s-=1
    e-=1
    if s == 0:
        print(arr[e])
    else:
        print(arr[e] - arr[s-1])

