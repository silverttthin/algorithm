import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
# 오름차순
# start = 1
# def print_num(n, start):
#     if start <= n:
#         print(start, end=" ")
#         print_num(n, start+1)
#     else:
#         return 0

# print_num(n, start)

# 내림차순
def print_num(num):
    if num>0:
        print(n - num + 1, end=" ") #
        print_num(num-1)
    else:
        return 0

print_num(n)