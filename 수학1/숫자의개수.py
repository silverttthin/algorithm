import sys, collections
sys.stdin = open('input.txt')

prod = 1
for i in range(3):
    prod *= int(input())

cnter = collections.Counter(map(int, str(prod)))

for i in range(0, 9+1):
    if i in cnter:
        print(cnter[i])
    else: 
        print(0)