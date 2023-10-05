import sys
sys.stdin = open('input.txt','r')

m,n = map(int, input().split())

chae = [1 for i in range(n+1)]
chae[0],chae[1] = 0,0
for i in range(2, int(n**0.5)+1):
    if chae[i]==1:
        for j in range(i*i, n+1, i):
            chae[j]= 0

sosu = [i for i in range(m, n+1) if chae[i] == 1]

print(len(sosu))