import sys
sys.stdin = open('input.txt','r')

def lcm(a,b):
    origin_a, origin_b = a, b
    while b:
        a,b = b, a%b
    return origin_a * origin_b //a

p, v, k = map(int, input().split())

# 도색, 광택이 모두 실패하는 주기는 lcm(p+1, v+1)이다.
cycle = lcm(p+1, v+1)

# 주기를 기점으로 도색 또는 광택만 실패하는 가짓수는 주기 // x+1 - 1
if k>=cycle:
    c = cycle // (v+1) - 1
    d = cycle // (p+1) - 1
else:
    c = k // (v+1)
    d = k // (p+1) 
# 이 시점의 c, d는 한 주기의 개수 이다.
# 따라서 따블하자 겸 주기의 개수(b)만큼 곱해줘야한다. 
b, q = divmod(k, cycle)

if b!=0:
    c *= b
    d *= b
    # 이때 나머지를 x+1로 나눈 몫만큼 나머지 하자 연필의 개수가 만들어진다.
    c += q // (v+1)
    d += q // (p+1) 

# 나머지 a는 b,c,d의 여사건이다.
a = k-(b+c+d)

print(a,b,c,d)
