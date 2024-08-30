import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(n))