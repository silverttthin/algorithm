import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

n = int(input())
m = [[0] * (n+1)]
for i in range(1, n+1):
    m.append([0]+ list(map(int,input().split())))
M = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):

        m[i][j] += m[i-1][j] + m[i][j-1] - m[i-1][j-1]

for _ in range(M):
    a,b,c,d = map(int,input().split())
    print(m[c][d] - m[c][b-1] - m[a-1][d] + m[a-1][b-1])
