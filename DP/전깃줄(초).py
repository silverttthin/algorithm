import sys
sys.stdin = open('input.txt','r')


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort() # 이걸 먼저 해서 전처리 해야 x가 겹치지 않게됨


y_lislength = [1]*(n+1)

for i in range(1, n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            y_lislength[i] = max(y_lislength[i], y_lislength[j]+1)

print(arr)
print(n-max(y_lislength))