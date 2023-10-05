import sys
sys.stdin = open('input.txt','r')

def f(start, end): 
    if start<=end:
        for i in range(1, 9+1):
            for j in range(start, end+1):
                print(f'{j} * {i} = ', end="")
                if j*i >=10:
                    print(j*i, end="   ")
                else:
                    print(f' {j*i}', end="   ")
            print()

    else:
        for i in range(1, 9+1):
            for j in range(start, end-1, -1):
                print(f'{j} * {i} = ', end="")
                if j*i >=10:
                    print(j*i, end="   ")
                else:
                    print(f' {j*i}', end="   ")
            print()




while 1:
    s,e = map(int,input().split())
    if 2<=s<=9 and 2<=e<=9 :
        f(s,e)
        break
    else:
        print('INPUT ERROR!')
    




