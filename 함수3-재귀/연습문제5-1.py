import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

def fibo(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2) # fibo(3) = 2


print(fibo(n))

