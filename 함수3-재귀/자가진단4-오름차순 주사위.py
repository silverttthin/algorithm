import sys
sys.stdin = open('input.txt','r')

n = int(input())
lst = [0] * n

def all_dice_except_duplicates(x):
    if x == n:
        for elem in lst:
            print(elem, end=" ")
        print()
    elif x == 0:
        for noon in range(1,6+1):
            lst[x] = noon
            all_dice_except_duplicates(x+1)
    else:
        for i in range(lst[x-1], 6+1):
            lst[x] = i
            all_dice_except_duplicates(x+1)

all_dice_except_duplicates(0)

