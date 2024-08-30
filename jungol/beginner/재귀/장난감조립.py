import sys
sys.stdin = open('input.txt','r')

import collections
N = int(input()) # 1~N-1은 모든 부품의 번호들, N은 완제품 번호
M = int(input()) # 관계 가짓수

parts = collections.defaultdict(int)
not_basic_part = []
adj_matrix = [[0 for i in range(N+1)] for i in range(N+1)]

for i in range(M):
    x,y,k = map(int,input().split())
    not_basic_part.append(x)
    adj_matrix[y][x] = k


def part_tracking(part, cnt):
    for i in range(1, N):
        if adj_matrix[i][part] != 0:
            part_tracking(i, cnt * adj_matrix[i][part])
    else:
        parts[part]+=cnt

for i in range(1, N):
    if adj_matrix[i][N] != 0:
        part_tracking(i, adj_matrix[i][N])

for part, cnt in sorted(parts.items()):
    if part not in not_basic_part:
        print(part, cnt)



# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 2 0 0 
# 0 0 0 0 0 2 0 0 
# 0 0 0 0 0 0 3 0 
# 0 0 0 0 0 0 4 5 
# 0 0 0 0 0 0 2 2 
# 0 0 0 0 0 0 0 3 
# 0 0 0 0 0 0 0 0 