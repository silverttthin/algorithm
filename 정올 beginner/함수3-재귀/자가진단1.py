import sys
sys.stdin = open('input.txt','r')

n = int(input())

def prt(x):
    if x == 0:
        return 0
    else:
        print('recursive')
        prt(x-1)

prt(n)