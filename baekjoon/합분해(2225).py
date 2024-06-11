import sys;sys.stdin=open('input.txt','r')

n, k  = map(int,input().split())

table = [[0]*k for _ in range(n)]
# 규칙을 적으며 찾기. 근데 적는것도 스마트하게
# 변수가 2개면 이중표 고려

for c in range(k):
    table[0][c] = c+1
for r in range(n):
    table[r][0] = 1

for i in range(1, n):
    for j in range(1, k):
        table[i][j] = (table[i-1][j]%1000000000 + table[i][j-1]% 1000000000) % 1000000000

print(table[n-1][k-1])
