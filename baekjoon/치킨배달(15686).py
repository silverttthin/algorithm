import sys;sys.stdin=open('input.txt','r')

# 치킨집들을 다 뽑고 (그냥 순회해서 좌표값 따로 저장해두기) 
# 이중 m개를 뽑아 후보들을 만들고 (By dfs, 조합)
# 이때의 도시치킨거리를 구해서 최소값 갱신해나가기 

n, m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
homes = [[i,j] for i in range(n) for j in range(n) if city[i][j]==1]
bbqs = [[i,j] for i in range(n) for j in range(n) if city[i][j]==2]
chosen_bbqs= []
ans = sys.maxsize

def distance(spot1, spot2):
    return abs(spot1[0] - spot2[0]) + abs(spot1[1] - spot2[1])


def dfs(cnt, idx):
    global ans
    if cnt == m:
        city_chicken_distance = 0
        # 각 집마다 치킨거리 구하기
        for home in homes:
            chicken_distance = sys.maxsize

            for chosen_bbq in chosen_bbqs:
                chicken_distance = min(
                    chicken_distance, distance(home, chosen_bbq))
                
            city_chicken_distance += chicken_distance
        
        ans = min(ans, city_chicken_distance)
        return

    # bbqs 에서 m개를 고르는 조합작업 -> dfs으로 구현
    for i in range(idx, len(bbqs)):
        chosen_bbqs.append(bbqs[i])
        dfs(cnt+1, i+1)
        chosen_bbqs.pop()

dfs(0,0)

print(ans)