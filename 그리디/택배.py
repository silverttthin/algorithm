import sys
sys.stdin = open('input.txt','r')


n, capacity = map(int,input().split())
infoNum = int(input())
infos = [list(map(int,input().split())) for _ in range(infoNum)]
villages = [0] * (n+1)
infos.sort(key=lambda x: x[1])
ans = 0
for start, end, amount in infos:
    max_deliveryBox = max(villages[start:end])
    truckSpace = capacity - max_deliveryBox

    for i in range(start, end):
        villages[i] += min(truckSpace, amount)
    ans += min(truckSpace, amount)

print(ans)
    

