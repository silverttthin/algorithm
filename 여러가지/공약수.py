import sys
sys.stdin = open('input.txt','r')

a, b = map(int,input().split())

def gcd(a,b): 
    while b:
        a, b = b, a%b
    return a

def lcm(a,b,c = gcd(a,b)):
    return a*b // c

print(lcm(a,b))