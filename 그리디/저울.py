import sys
sys.stdin = open('input.txt','r')

n = int(input())

weights = list(map(int,input().split()))

weights.sort()

# 정렬했을 때 첫 무게추가 1이 아니면 답은 무조건 1
# 어떤 무게추가 n일 때 다음 무게추가 

if weights[0] != 1:
    print(1)
    exit()

for idx, weight in enumerate(weights):
    key = sum(weights[:idx]) + 1
    if weight >= key + 1 :
        print(key)
        exit()

print(sum(weights) + 1)