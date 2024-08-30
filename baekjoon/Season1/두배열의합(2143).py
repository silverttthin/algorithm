import sys;sys.stdin=open('input.txt','r')

import bisect

T = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b= list(map(int,input().split()))

a_prefix_sums = []
b_prefix_sums = []

# 누적합 -> 배열 길이가 10^3이라 2 * n^2으로 가능
for i in range(n):
    for j in range(i+1, n+1):
        a_prefix_sums.append(sum(a[i:j]))

for i in range(m):
    for j in range(i+1, m+1):
        b_prefix_sums.append(sum(b[i:j]))

# 정렬 -> 누적합 길이가 1억미만이면 안전
a_prefix_sums.sort()
b_prefix_sums.sort()

ans = 0
for i in range(len(a_prefix_sums)):
    tmp = T-a_prefix_sums[i]
    l = bisect.bisect_left(b_prefix_sums, tmp)
    r = bisect.bisect_right(b_prefix_sums, tmp)
    ans += (r-l)
    # 누적합 결과가 같은게 여러개일수도
    # upperbound는 해당값 +1 idx 리턴 -> 그냥 r-l하면 딱 개수만큼

print(ans)


