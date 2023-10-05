import sys
sys.stdin = open('input.txt','r')

tmp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while 1:
    ans = ''
    line = input().split()
    if line== ['0']:
        break
    
    a, s, b = line
    a, b = map(int, (a,b))

# 1) a진법 수를 10진법으로 변환- int 사용하거나 호너법칙으로 직접구현
    s = int(s, a)

    if s == 0:
        print(0)

# 2) 변환한 수를 b진법으로 변환- stirng.digits + string.ascii_uppercase 사용기믹
    else:
        while s:
            q, r = divmod(s, b)
            ans += tmp[r]
            s = q
        print(ans[::-1])