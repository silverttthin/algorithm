import sys
sys.stdin = open('input.txt','r')

n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
lst.sort(key = lambda x: x[1])

# 다음 물질의 최저온도가 이전 물질의 최고온도 이하이면 냉장고가 안늘엉남

refrig = 0
prevMaxTemperature = -271

for x,y in lst:
    if x>prevMaxTemperature:
        refrig += 1
        prevMaxTemperature = y
    elif x<=prevMaxTemperature<=y:
        continue

print(refrig)



