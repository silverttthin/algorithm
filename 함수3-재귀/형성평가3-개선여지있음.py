import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())

lst = [0] * n
def dice_sum(x):
    if x == n+1:
        if sum(lst) == m:
            for elem in lst:
                print(elem, end=" ")
            print()
        return
    
    for noon in range(1,6+1):
        lst[x-1] = noon
        dice_sum(x+1)


dice_sum(1)