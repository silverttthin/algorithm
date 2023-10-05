import sys
sys.stdin = open('input.txt', 'r')

def gcd(a, b):
    a, b = max(a,b), min(a,b)
    r = a%b
    if r == 0:
        return b
    elif r != 0:
        return gcd(b, r)
    

n = int(input())
lst = list(map(int, input().split()))


total_gcd = lst[0]
total_lcm = lst[0]

for elem in lst[1:]:
    total_gcd = gcd(total_gcd, elem)
    total_lcm = total_lcm*elem // gcd(total_lcm, elem) ## lcm구하는거 다시보기

    

print(total_gcd, total_lcm)




