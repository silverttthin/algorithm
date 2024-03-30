import sys
sys.stdin = open("input.txt",'r')

from collections import defaultdict

n = int(input())

chrs = [input() for _ in range(n)]

# 단어들이 나온 위치들 조사해 가중치부여
# 가중치가 높은 알파벳부터 정렬하기
d = defaultdict(int)

for chr in chrs:
    l = len(chr)
    for idx, c in enumerate(chr):
        # 10^(l-1-idx)만큼 각 자리에 가중치부여하기
        d[c] += 10**(l-1-idx)
    
words_sort = sorted(d.values(), reverse=True)

ans = 0
n = 9
for k in words_sort:
    ans += k * n
    n-=1
print(ans)





