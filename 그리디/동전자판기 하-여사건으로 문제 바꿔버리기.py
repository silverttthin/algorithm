import sys
sys.stdin = open('input.txt','r')

price = int(input())
tmp = list(map(int,input().split()))

# 입력 - {(전체 -w)을 최소 동전 개수로 사용(큰동전부터)} = 최대 동전 개수로 w원
wallet = {coin : amount for coin, amount in zip([500,100,50,10,5,1],tmp)}
walletSum = 0
for coin, amount in zip([500,100,50,10,5,1],tmp):
    walletSum += coin * amount

price2 = walletSum - price

for coin, amount in wallet.items():
    for i in range(1, amount+1):
        if price2 >= coin:
            price2 -= coin
            wallet[coin] -= 1

print(sum(wallet.values()))
for i in wallet.values():
    print(i, end=" ")
