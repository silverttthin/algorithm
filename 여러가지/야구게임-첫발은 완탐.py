import sys
sys.stdin = open('input.txt', 'r')

# 123부터 987까지
# 모든 숫자들을 하나씩
# 질문한 숫자들에 대조해 SB카운트를 계산해
# 어떤 숫자가 질문한 모든 숫자들의 SB카운트들과 같다면 
# 해당 숫자는 영수가 생각하고 있을 가능성이 있는 숫자이므로 ans +=1

# [구현사항]
# v 123-987까지 모든 숫자들을 하나씩 순회 (대조하는 숫자를 candidate라 함)
# v 질문한 수(question_num)와 candidate를 비교
# v 비교해 SB카운트 내는 함수 yagu() 구현
# - 첫 비교가 맞다면 다음 비교로 넘어가는 동작 
# - 모든 비교가 맞는 체크하는 로직
# - 모든 비교가 맞다면 ans += 1

def yagu(a, b):
    strike, ball = 0, 0
    a = list(map(int, str(a)))
    b = list(map(int, str(b)))

    check = [-1 for _ in range(10)]

    for idx, sub_a in enumerate(a):
        check[sub_a] = idx
    
    for idx, sub_b in enumerate(b):
        if check[sub_b] >= 0 and check[sub_b] == idx:
            strike += 1
        elif check[sub_b]>=0 and check[sub_b] != idx:
            ball += 1

    return (strike, ball)


n = int(input())
ans = 0

nums = []
for i in range(1, 9+1):
    for j in range(1, 9+1):
        for k in range(1, 9+1):
            if i==j or j==k or i==k :
                continue
            nums.append(i*100 + j*10 + k)

conditions = [list(map(int, input().split())) for _ in range(n)]

for num in nums:
    for condition, strike, ball in conditions:
        if yagu(num, condition) != (strike, ball):
            break
        
    else :
        ans += 1

print(ans)

