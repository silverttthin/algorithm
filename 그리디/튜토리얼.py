import sys
sys.stdin = open('input.txt','r')

import collections

weights = collections.defaultdict(int)
line = list(map(int,input().split()))

n = line[5]
for cnt, weight in zip(line[:-1], [1,2,4,8,16]):
    weights[weight] += cnt

weights = list(weights.items())[::-1]

ans = 0
for weight, cnt in weights:
    for i in range(1, cnt+1):
        if weight > n: break
        ans += 1
        n -= weight
    
if n == 0 : print(ans)
else: print('impossible')



# 16 10
# 8 0
# 4 10
# 2 10
# 1 10