import sys
sys.stdin = open('input.txt','r')

x,y = map(int,input().split())
z = 20091024
def half(x,y):
    if y ==0 : return 1
    tmp = half(x,y//2)
    if y %2 == 0:
        return tmp * tmp % z
    elif y%2 ==1:
        return tmp*tmp*x % z
    
# 긴수도 제공하지만 연산이 오래걸림
print(half(x,y))