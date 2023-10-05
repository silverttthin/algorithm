import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

memo = [0] * (n+1)
memo[1]= 1

def print_nth_elem(x):
    if x == 1:
        return 1
    else:
        if memo[x]!= 0:
            return memo[x]
        else:
            memo[x] = print_nth_elem(x//2) + print_nth_elem(x-1)
            return memo[x]

print(print_nth_elem(n))

