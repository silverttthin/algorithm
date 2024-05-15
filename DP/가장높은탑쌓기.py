import sys
sys.stdin = open('input.txt','r')

n = int(input())

blocks = [list(map(int,input().split())) + [i+1] for i in range(n)]


blocks.sort(reverse=True)

# ith 벽돌까지 쓸 때의 가능한 최고높이
height_LTS = [0 for i in range(n)]
prev_j = [-1]*n # ith까지의 LIS의 [-2]번째 요소

for idx, block in enumerate(blocks):
    height_LTS[idx] += block[1]

# 밑면넓이는 쌓을수 있게 정렬된 상태
# 무게가 쌓을 수 있을때 높이를 비교해 높이 lis 
for i in range(1, n):
    for j in range(i):
        if blocks[j][2] > blocks[i][2] and height_LTS[i] < height_LTS[j]+blocks[i][1]:
            height_LTS[i] = height_LTS[j]+blocks[i][1]
            prev_j[i] = j

max_idx = height_LTS.index(max(height_LTS))
x = max_idx
used_blocks = []
while 1:
    used_blocks.append(blocks[x][3])
    x = prev_j[x]
    if x<0: break

print(len(used_blocks))
for n in used_blocks:
    print(n)