import sys
sys.stdin = open('input.txt','r')

from collections import Counter
scores = []
deck = []

for i in range(5):
    deck.append(input().split())

chrs = list(zip(*deck))[0]
nums = list(map(int, list(zip(*deck))[1]))

nums.sort()
cnter = Counter(nums).most_common()

# 1. 모두 같은색 and 연속된 숫자
if all(c == chrs[0] for c in chrs) and all(nums[i-1] + 1 == nums[i] for i in range(1,5)):
    scores.append(900 + max(nums))

# 2. 5장중 4장의 숫자가 같음
elif cnter[0][1] == 4:
    scores.append(800+cnter[0][0])

# 3. 숫자가 풀하우스
elif cnter[0][1] == 3 and cnter[1][1]==2:
    scores.append(cnter[0][0] * 10 + cnter[1][0] + 700)

# 4. 카드색 모두 같은 경우
elif all(c == chrs[0] for c in chrs) :
    scores.append(max(nums) + 600)

# 5. 연속된 숫자
elif all(nums[i-1] + 1 == nums[i] for i in range(1,5)):
    scores.append(max(nums) + 500)

# 6. 5장 중 3장이 같은 수
elif cnter[0][1] == 3 :
    scores.append(cnter[0][0] + 400)

# 7. 5장 중 2장이 같고 다른 두장이 같을 때
elif cnter[0][1] == 2 and cnter[1][1] == 2:
    scores.append(cnter[1][0] * 10 + cnter[0][0] + 300)

# 8. 5장 중 2장이 같을 때
elif cnter[0][1] == 2:
    scores.append(cnter[0][0]+ 200)
else:
    scores.append(max(nums) + 100)
print(max(scores))