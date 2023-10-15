import sys
sys.stdin = open('input.txt','r')

n = int(input())

def hanoi(x, a,b,c):
    if x ==0: return
    hanoi(x-1, a,c,b)
    print(f'{x} : {a} -> {c}')
    hanoi(x-1, b, a, c)



hanoi(n, 1,2,3)