import sys
sys.stdin = open('input.txt','r')

n = int(input())

lst = [0] * 100001
lst[0] = -1
lst[1] = 1
lst[2] = 3
for i in range(3, 100001):
    if lst[i] == 0:
        lst[i] = (lst[i-1]+2*lst[i-2])%20100529

print(lst[n])