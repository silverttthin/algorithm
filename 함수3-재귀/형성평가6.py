import sys
sys.stdin = open('input.txt', 'r')

lst = list(map(int, input().split()))

product = 1
for num in lst:
    product *= num

def unitProduct(x):
    if x == 0:
        return 1
    else:
        q, r = divmod(x, 10) # 136 //10 = 13, r = 6
        if r == 0:
            return unitProduct(q)
        else:
            return unitProduct(q) * r

print(unitProduct(product))