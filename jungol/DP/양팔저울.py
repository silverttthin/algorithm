import sys
sys.stdin = open('input.txt','r')

w_n = int(input()) # 추 개수는 30 이하
weights = list(map(int,input().split())) # 추는 500이하
marble_n = int(input()) # 구슬 개수는 7 이하
marbles = list(map(int,input().split())) # 구슬무게는 40,000 이하

dp = ['N'] * (sum(weights) + 1)# i라는 무게가 가진 추로 가능한지 여부 저장함
dp[0] = 'Y'

for weight in weights:
    tmp = set()
    for marble_w in range(len(dp)):
        if dp[marble_w] == 'Y': # 구슬 무게는 최대 4만, dp길이는 최소 4만
            tmp.add(abs(marble_w - weight))
            if marble_w+ weight <= len(dp):
                tmp.add(marble_w+weight)

    
    for i in tmp:
        dp[i] = 'Y' # i 최대는 

for i in marbles: 
    if i>=len(dp): print('N', end= " ")
    else:
        print(dp[i], end=" ") # 

# tmp배열은 각 무게추를 순회해 기존조합가능한 무게들을 최신화하며 새로운 조합가능한 무게들을 추가
# 배낭문제의 row는 각 보석들을 순회해 기존 조합가능한 무게-가치 쌍을 최신화하며 더 높은 가치들을 추가


