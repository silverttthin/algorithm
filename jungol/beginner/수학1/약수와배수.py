import sys
sys.stdin = open('input.txt','r')

N = int(input())
lst= list(map(int, input().split()))
num= int(input())
sum_divisor = 0
sum_multiple = 0

for elem in lst:
    if num % elem == 0: sum_divisor += elem
    if elem % num == 0: sum_multiple += elem

print(sum_divisor)
print(sum_multiple)