import sys;sys.stdin = open("input.txt",'r')

n = int(input())

arr = list(map(int,input().split()))

subSum = arr[:]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and subSum[j]+arr[i] > subSum[i]:
            subSum[i] = subSum[j] + arr[i]


print(max(subSum))