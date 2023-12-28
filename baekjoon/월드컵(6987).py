import sys
sys.stdin = open('input.txt','r')

cb = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],
    [1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
ans = []

def dfs(stage):
    global teams, flag
    if stage == 15:
        for team in teams :
            if team != [0,0,0] : 
                return 0
                
        
        return 1
    

    team1, team2 = teams[cb[stage][0]], teams[cb[stage][1]]
    for x,y in [[0,2], [2,0], [1,1]]:
        if team1[x] > 0 and team2[y] > 0:
            team1[x] -= 1
            team2[y] -= 1

            if dfs(stage + 1) == 1:
                return 1

            team1[x] += 1
            team2[y] += 1
    return 0

for _ in range(4):
    tmp = list(map(int,input().split()))
    teams = [tmp[i:i+3] for i in range(0,16,3)]

    ans.append(dfs(0))

print(*ans)