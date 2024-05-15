import sys;sys.stdin = open('input.txt','r')

from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))

ansarr= []


for i in range(n):
    tmp = bisect_left(ansarr, arr[i])    
    if tmp == len(ansarr):
        ansarr.append(arr[i])
    else:
        ansarr[tmp] = arr[i]

print(len(ansarr))