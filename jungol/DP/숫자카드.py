import sys
sys.stdin = open('input.txt','r')

# i번째 숫자를 기준으로
# d[i] = i번째 수 단독(=d[i-1]) + 'i, i-1글자' 가능한경우(=d[i-2]
# 가능한지는 숫자화 해서 34이하 양의정수인지 판별하기로

n = input().rstrip()
d = [0] * (len(n) + 1)

def check(i):
    return True if 10<=int(n[i-1]) * 10 + int(n[i])<=34 else False

if n[0] != '0':
    d[0] = 1
    d[1] = 1
else:
    print(0)
    exit()

for i in range(2, len(n)+1):
    if n[i-1] == '0' and check(i-1) == False : 
        print(0)
        exit()
    if n[i-1] != '0':
        d[i] += d[i-1]

    if check(i-1):
        d[i] += d[i-2]

print(d[-1])



