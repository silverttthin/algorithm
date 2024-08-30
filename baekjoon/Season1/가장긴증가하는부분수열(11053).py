import sys;sys.stdin = open('input.txt','r')


n = int(input())
arr = list(map(int,input().split()))

length = [1]*n


for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and length[i]<length[j]+1:
            length[i] = length[j]+1

print(max(length))