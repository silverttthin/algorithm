import sys
sys.stdin = open('input.txt','r')

n, p = map(int,input().split())

check = [0 for _ in range(1000001)]

def cycle(x):
    global ans
    if check[x] == 2:
        # for flag in check:
        #     if flag == 2:
        #         ans+=1
        print(check.count(2))
        exit()

    check[x]+=1
    cycle((x * n) % p)

cycle(n)