import sys
sys.stdin = open('input.txt','r')

n = int(input())

def desc_order(x):
    if x==0:
        return 1
    else:
        desc_order(x-1)
        print(x, end=" ")

desc_order(n)