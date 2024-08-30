import sys
sys.stdin = open('input.txt','r')

n = int(input())

ans = 0
col = [0 for _ in range(n+1)]

# 대각선의 법칙
yX_diagonal = [0 for _ in range(2*n-1)]
# yX는 합이 같으므로 0~2n-2까지 
y_x_diagonal = [0 for _ in range(2*n)] 
# y-X는 차가 같으므로 -(n-1) ~ n-1, 음수 인덱스 처리위해 값은 n-1만큼 더해진 것으로 봄

def queen(x): # x행에 퀸을 둘 곳을 탐색하고 다음 퀸으로 넘어간다
    global col, yX_diagonal, y_x_diagonal, ans
    if x == n: # 모든 퀸을 다 놨다면 올바른 경우수 하나가 추가된다.
        ans += 1
        return
    
    for i in range(n): # x행의 i열 작업
        if col[i] != 1 and yX_diagonal[x+i] !=1 and y_x_diagonal[x-i+n-1]!=1:
            # 열, 대각선 체크 배열의 검사에 모두 통과하면 현재 x열 i행은 둘 수 있다는 뜻
            col[i]+=1
            y_x_diagonal[x-i+n-1]+=1
            yX_diagonal[x+i]+=1

            queen(x+1) # 체크해두고 다음 퀸으로 넘어가기

            # 그다음 열로 넘어가기 전에 이전에 뒀던 퀸의 흔적은 해제하기
            col[i]-=1
            y_x_diagonal[x-i+n-1]-=1
            yX_diagonal[x+i]-=1

queen(0)
print(ans)