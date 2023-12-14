import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

def divto10(x):
    if x == 0:
        return 0
    else:
        q = x//10
        r = x%10
        return r**2 + divto10(q)

print(divto10(n))
