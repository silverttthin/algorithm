import sys
sys.stdin = open('input.txt', 'r')

a= int(input())
b= int(input())
ans = a*b
for _ in range(3):
    print(a *(b%10))
    b //=10
print(ans)


