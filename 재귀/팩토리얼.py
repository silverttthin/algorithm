import sys
sys.stdin = open('input.txt','r')

n = int(input())

def facto(x):
    if x>1:
        print(f'{x}! = {x} * {x-1}!')
        return x * facto(x-1)
    print('1! = 1')
    return 1

print(facto(n))