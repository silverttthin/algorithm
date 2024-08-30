import sys;sys.stdin=open('input.txt','r')

from collections import defaultdict

weight_map = defaultdict(int)

n = int(input())
words = [input() for _ in range(n)]

for word in words:
    l = len(word)
    for idx, c in enumerate(word):
        weight_map[c] += 10**(l-1-idx) # defaultdict를 쓴 이유
        # 각 알파벳의 위치의 자릿수를 더해간다 

weight_map = sorted(weight_map.values(), reverse=True)

# 가중치비교해 알파벳에 값을 부여해 계산하기보다
# !!=> 이미 구한 내림차순 가중치 배열에 9부터 더하면 됨
# 이미 해당 알파벳이 words의 각 단어에서 위치한 자릿수는 결정된 상태이니
# 자릿수가 가장 큰 순서대로 그리디하게 9부터 내림차순으로 부여하면 되니

ans, num = 0, 9
for digit in weight_map:
    ans += num * digit
    num-=1
print(ans)




