import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int,input().split())
dices=[0 for i in range(n)]
def dice(level):
    if level>n:
        if sum(dices) == m:
            for num in dices:
                print(num, end=" ")
            print()
            return 1 
        else:
            return 0

    for i in range(1,6+1):
        dices[level-1] = i
        if dice(level+1) ==1 :
            break


dice(1)