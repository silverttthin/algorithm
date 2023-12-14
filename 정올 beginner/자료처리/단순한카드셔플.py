import sys
sys.stdin = open('input.txt','r')

n = int(input())

deck = [i+1 for i in range(n)]

ans = []

while 1:
    ans.append(deck.pop(0))
    if deck:
        deck.append(deck.pop(0))
    else:
        break

for card in ans:
    print(card, end=" ")
