import sys
import collections
sys.stdin = open('input.txt','r')

T = int(input())

# 계산식 : 각 카테고리 별 의상수 +1들의 곱 -1

for _ in range(T):
    d= collections.defaultdict(list)
    costumes= int(input())
    for _ in range(costumes):
        a, b = input().split()
        d[b].append(a)

    prod = 1
    for clothes in d.values():
        prod *=(len(clothes) + 1)
    
    print(prod-1)
        


        


