import sys
sys.stdin = open('input.txt','r')

n, s = map(int,input().split())
# n은 총 주차 수, s는 1주 보관비용
arr = [list(map(int,input().split())) for _ in range(n)]
cost = 0
# c, y는 가격, 필요한 우유
best_price = 100000000
for idx, (c,y) in enumerate(arr):
    best_price = min(best_price, c)
    cost += best_price * y
    best_price += s

print(cost)
