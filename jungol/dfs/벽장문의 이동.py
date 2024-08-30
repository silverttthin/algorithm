import sys
sys.stdin = open('input.txt','r')

closets = [0] * (int(input()) + 1)

left,right = map(int, input().split()) # 초기에 열린 벽장들

n = int(input()) # 사용할 벽장들의 개수

to_be_usedClosets = [int(input()) for _ in range(n)]
ans = 1000000000

def dfs(x, left, right, movement): # 열어야할 x번째 벽장을 처리하는 함수
    global ans

    if ans < movement:
        return
    
    if x == n:
        ans = movement
        return

    if right <= to_be_usedClosets[x]:
        movement += to_be_usedClosets[x] - right
        right = to_be_usedClosets[x]
        dfs(x+1, left, right, movement)
        
    
    elif to_be_usedClosets[x] <= left:
        movement += left - to_be_usedClosets[x]
        left = to_be_usedClosets[x]
        dfs(x+1, left, right, movement)
    
    else: # 열린문이 left,right사이일땐 dfs두번 다 해봐야함. 차후에 뭘 움직인게 낫게 평가될지 알 수 없으니
        dfs(x+1, to_be_usedClosets[x], right, movement + abs(left - to_be_usedClosets[x])) # left가 열린문이 될때
        dfs(x+1, left, to_be_usedClosets[x], movement + abs(to_be_usedClosets[x] - right))  # right가 열리문이 될때

dfs(0, left, right, 0)
print(ans)