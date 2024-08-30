import sys
sys.stdin = open('input.txt','r')

n = int(input())

def unit_sum(x):
    if x==0: return 0
    return x%10 + unit_sum(x//10)
print(unit_sum(n))