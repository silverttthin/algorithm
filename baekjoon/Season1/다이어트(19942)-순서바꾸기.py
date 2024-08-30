import sys
sys.setrecursionlimit(50000)

sys.stdin = open('input.txt','r')

n = int(input())
min_nutrients= list(map(int,input().split()))
ingredients = [list(map(int,input().split())) for _ in range(n)]

ans = [0] * n
tmp = [0] * n
ans_cost = 123456789

def check(nutrient, cost):
    global ans_cost

    for j in range(4):
        if min_nutrients[j] > nutrient[j]:
            return
    
    if cost < ans_cost:
        ans_cost = cost
        ans[:] = tmp[:]

def dfs(i, nutrient, cost):
    global tmp

    if i == n:
        return
    
    tmp[i] = 0
    check(nutrient, cost)
    dfs(i+1, nutrient, cost)

    for j in range(4):
        nutrient[j] += ingredients[i][j]
    cost += ingredients[i][4]
    tmp[i] = 1
    check(nutrient, cost)
    dfs(i+1, nutrient, cost)





    

dfs(0, [0,0,0,0], 0)

if ans_cost == 123456789:
    print(-1)
    exit()
    
print(ans_cost)
for idx, num in enumerate(ans):
    if num == 1:
        print(idx+1, end=" ")
