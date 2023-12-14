import sys
sys.stdin = open('input.txt','r')

n = int(input())

def allsum(x):
    if x == 1:
        return 1
    return x + allsum(x-1)

print(allsum(n))