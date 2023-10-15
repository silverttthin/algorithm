import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())

lst = [0 for i in range(n)]

if m == 1:
    def dice(x):
        if x >n :
            for val in lst:
                print(val, end=" ")
            print()

        else:
            for i in range(1,6+1):
                lst[x-1] = i
                dice(x+1)
    dice(1)

elif m ==2:
    def dice_2(x): 
        if x >n :
            for val in lst:
                print(val, end=" ")
            print()

        else:
            for i in range(1,6+1): 
                if x !=1 and i<lst[x-2]:
                    continue
                else:
                    lst[x-1] = i
                    dice_2(x+1)
    dice_2(1)



else :
    def dice_3(x): # 현재 레벨의 눈은 전 레벨의 눈 이상이여야 한다.
        if x >n :
            if len(set(lst))==n:
                for val in lst:
                    print(val, end=" ")
                print()

        else:
            for i in range(1,6+1): 
                lst[x-1] = i
                dice_3(x+1)
    dice_3(1)