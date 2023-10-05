import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

memo = [0] * (n+1)
memo[1] = 1
memo[2] = 2

def seq(x):
    if memo[x] == 0:
        memo[x] = (seq(x-1) * seq(x-2)) % 100
        return memo[x]
    elif x==1: return 1
    elif x==2: return 2
    
    else:
        return (memo[x-1] * memo[x-2]) % 100
    


print(seq(n))