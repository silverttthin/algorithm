import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

def divTilZero(n):
    if n == 1: return 0
    elif n%2 == 0: return divTilZero(n//2) + 1
    elif n%2 != 0 : return divTilZero(n//3) + 1

print(divTilZero(n))