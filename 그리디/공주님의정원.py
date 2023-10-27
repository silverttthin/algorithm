import sys
sys.stdin = open('input.txt','r')


n = int(input())
ans = 0
flowers = [list(map(int,input().split())) for _ in range(n)]
flowers.sort()

# 포인트가 넘기 직전까지의 꽃들 중 지는 시기가 제일 늦은것만을 고르자
point = [3,1] 
latest = [0,0] 
for idx in range(n):
    sM,sD,eM,eD = flowers[idx]
    if point<[sM,sD] and [sM,sD] <= latest: # 개화시작이 latest보다 늦으면 불연속
        ans+=1
        point = latest[:]
        # point보다 빠른 개화일 중 end가 제일 늦은 꽃 고르기
    latest = max(latest, [eM,eD])
else:# ans판별에서 누락된 끝 요소 검사
    # 이미 11월30일까지 피는 꽃들이 택돼있으면 더는 고르면 안돼
    if point < [12,1]: 
        sM,sD,eM,eD = flowers[-1]
        if [sM,sD] <= point and [11,30]<[eM,eD]:
            ans += 1
            point = [eM,eD]
        else:
            ans = 0

print(ans)