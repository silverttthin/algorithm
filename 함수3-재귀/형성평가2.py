import sys
sys.stdin = open('input.txt', 'r')
# 이전단계들에 영향을 미치고자 하는 경우에 리턴문적기

n = int(input())

def all_prt(x):
    if x == 1 or x == 2:
        print(x, end=" ")
    
    else:
        all_prt(x-2)
        print(x,end=" ")

all_prt(n)