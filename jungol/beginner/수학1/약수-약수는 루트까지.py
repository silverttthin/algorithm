import sys
import math
sys.stdin = open('input.txt', 'r')

n = int(input())

root = math.sqrt(n)
lst = []
other_lst = []

for i in range(1, int(root +1)):
    if n % i ==0:
        lst.append(i)
        other_lst.append(n / i)
other_lst = list(map(int, other_lst))

other_lst.sort()
if lst[-1] == other_lst[0]:
    lst.pop()

lst = lst + other_lst

for num in lst:
    print(num, end=" ")

# 최적화
# def get_yaksu(num):
#     yaksu = []
#     root = math.sqrt(num)
#     for i in range(1, int(root)+1):
#         if num % i ==0:
#             yaksu.append(i)
#             if i != root:
#                 yaksu.append(num//i)
                
#     yaksu.sort()
#     return(yaksu)
