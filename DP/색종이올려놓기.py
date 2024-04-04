import sys
sys.stdin = open('input.txt','r')

# LIS 응용해 색종이 쌓아올리기
n = int(input())

papers= [list(map(int,input().split()))  for _ in range(n)]
for i, paper in enumerate(papers):
    a,b = paper
    if a>b:
        papers[i][0], papers[i][1] =papers[i][1], papers[i][0] 
papers.sort()

LIScnt = [1] * (n+1)

for i in range(1, n):
    for j in range(i):
        if papers[j][0]<=papers[i][0] and papers[j][1]<=papers[i][1]:
            LIScnt[i] = max(LIScnt[i], LIScnt[j]+1)

print(max(LIScnt))