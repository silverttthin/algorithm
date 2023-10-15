import sys
sys.stdin = open('input.txt','r')

N = int(input())
second_line_list = [int(input()) for i in range(N)]

ans = []
# 2처럼 이미 사이클 리스트에 있는 애로 향하는 노드는 그냥 리턴으로 끝내버리기

def pick(n): 
    global arrival_cnt  
    if arrival_cnt[n] != 2:
        if second_line_list[n-1] in ans:
            return
        arrival_cnt[n] += 1
        pick(second_line_list[n-1])
    else:
        # 현재 도착 2번한 모든 노드들 추가하기
        for idx, val in enumerate(arrival_cnt):
            if val == 2:
                ans.append(idx)

        

for i in range(1, N+1):
    arrival_cnt = [0 for _ in range(N+1)]
    pick(i)

ans.sort()

print(len(ans))
for val in ans:
    print(val, end='\n')