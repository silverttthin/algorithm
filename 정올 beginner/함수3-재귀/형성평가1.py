import sys
sys.stdin = open('input.txt', 'r')
# 이전단계들에 영향을 미치고자 하는 경우에 리턴문적기

n = int(input())

def prt(x):
    # 먼저 나눈값을 호출하고 그다음에 현재값을 출력?
    if x==1:
        print(x, end=" ")
        return 0
    prt(x//2)
    print(x, end=" ")

prt(n)




