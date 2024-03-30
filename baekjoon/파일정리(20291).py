import sys
sys.stdin = open('input.txt','r')

from collections import defaultdict

n = int(input())
lst= [input() for _ in range(n)]

d = defaultdict(int)

for file in lst:
    for idx, c in enumerate(file):
        if c == '.':
            extension = file[idx+1:]
            d[extension] += 1

d = list(d.items())
d.sort(key= lambda x: x[0])
for i in d:
    print(i[0], i[1])