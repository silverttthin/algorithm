import sys
sys.stdin = open('input.txt', 'r')

m,s,c = map(int,input().split())

# 차잇값들을 내림차순 정렬한후
# 큰값부터 M-1개를 고른 합을 [l,r]에서 빼기
cows = []
diff = []
prev_c= -1

for i in range(c):
    cow = int(input())
    cows.append(cow)

cows.sort()
for i, cow in enumerate(cows):
    if not prev_c == -1:
        diff.append(cow - prev_c -1)
    prev_c = cow

diff.sort(reverse=True)

ans = cows[-1] - cows[0] +1
try:
    for i in range(m-1):
        ans -= diff[i]
except:
    pass
print(ans)