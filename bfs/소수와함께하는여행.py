import sys
sys.stdin = open('input.txt','r')

from collections import deque

start, end = map(int,input().split())

visited = [False] * 10001
visited[start] = True

chae = [True] * 10000
chae[0],chae[1] = False,False
for i in range(2, 100):
    if chae[i] == True:
        for j in range(i*i, 10000, i):
            chae[j] = False

def movable(a,b):
    a=str(a)
    b=str(b)

    diff_cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            diff_cnt += 1
    if diff_cnt == 1 :
        return True
    else:
        return False

def bfs(s,end):
    q = deque([[s,0]])
    # 큐에서 팝한 x를 1000~9999까지 돌며
    # 한번에 이동할 수 있는지 보며 큐에 넣기

    # 한번에 이동하는 조건은
    # 두 수를 리스트화했을 때 동시에 순회하며
    # 다른 수가 딱 한 개 있을때 성립
    # 근데 천의자릿수는 0일 수 없으니 따로 체크

    while q:
        x, cnt = q.popleft()
        if x == end:
            return cnt

        for i in range(1000, 10000):
            if chae[i] == True and visited[i] == False and movable(x, i):
                q.append([i, cnt+1])
                visited[i] = True




print(bfs(start,end))
