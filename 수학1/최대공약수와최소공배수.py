import sys
import math
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())


# def gcd(a, b):
#     a, b = max(a,b), min(a,b)
#     r = a%b
#     if r == 0:
#         return b
#     elif r != 0:
#         return gcd(b, r)

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

ab_gcd = (gcd(a,b))

print(ab_gcd)
print(a*b //ab_gcd)



# a를 b로 나눈 몫 q과 나머지 r가 나온다.
# r이 0이 아니라면 계속 b와 r을 나눠야한다.
# r이 0이라면 b가 gcd다.
# r이 0이 아니라면 b와 r을 나눈다.





# max_val = -1

# x= min(a,b)
# for i in range(1, x+1):
#     if a%i==0 and b%i==0:
#         max_val = i
# print(max_val)





# multiple = 1
# while 1:   
#     if a*multiple % b ==0:
#         print(a*multiple)
#         break
#     multiple += 1
