import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
# 기억해두는 리스트
memoization = [0 for _ in range(n+1)]
memoization[1], memoization[2] = 1, 1

def fibo(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    else:
        if memoization[x] !=0:
            return memoization[x]
        else:
            memoization[x] = fibo(x-1) + fibo(x-2)
            return  memoization[x]



print(fibo(n))

