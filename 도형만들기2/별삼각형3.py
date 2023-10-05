import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
if n >100 or n %2 ==0:
    print('INPUT ERROR!')
    exit()

star_cnt = 1
space_cnt = 0

for i in range(1, n+1):
    print(f'{" " *space_cnt}{"*" * star_cnt}')

    if i > int(n/2):
        star_cnt -=2
        space_cnt -= 1
    else:
        star_cnt += 2
        space_cnt += 1

