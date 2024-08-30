import sys

sys.stdin = open('input.txt', 'r')

h, m = map(int, input().split())

if h<=100 and 1<=m<=3:
    if m ==1 :
        for i in range(1, h+1): print('*' * i)
    
    elif m ==2:
        for i in range(h, 0, -1): print('*' * i)
    
    elif m ==3:
        star_cnt, space_cnt = 1, h-1
        for _ in range(h):
            print(" " * space_cnt + '*' * star_cnt)
            star_cnt += 2
            space_cnt -= 1


else:
    print('INPUT ERROR!')
