import sys
sys.setrecursionlimit(10000)

sys.stdin = open('input.txt', 'r')


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = -1

y_x_diagonal = [0 for _ in range(2*n)]  # 감소 사선은 차가 같음. 근데 음수 표현을 위해 음수 부분은 n-1을 더하는 식으로 처리하기.
# 최소가 -(n-1)이므로 0부터 시작하는 인덱스에 저장하려면 n-1을 더해줘야하니까


# row가 n이면 col을 증가시킨다.
# col이 최대가 되면 ans를 이전값과 비교해 갱신한다. 그리고 리턴한다.
# 비숍을 두면 사선법칙 체크리스트에 표시를 한다.
# 표시된 사선은 비숍을 둘 수 없다.

# able_spots를 하나씩 돌며 체크배열에 체크를 해줌. 
# 다음 dfs로 들어감
# 비숍을 둘수 있는지 체크할때 체크배열 검사를 통과해야함

def bishop(row,col, bishop_cnt):
    global ans, y_x_diagonal

    flag = False

    if col == n-1:
        ans = max(ans, bishop_cnt)
        return

    if row < n:
        r, c = row, col

        while 0<=r<n and 0<=c<n:
            if board[r][c] == 1:
                if y_x_diagonal[r-c+n-1]!=1 :
                    y_x_diagonal[r-c+n-1] = 1
                    bishop(row+1,col,bishop_cnt+1)
                    y_x_diagonal[r-c+n-1] = 0
                    flag = True
            r-=1
            c+=1
        
        if flag == False: # 사선에 둘 1이 하나도 없었다면
            bishop(row+1, col, bishop_cnt) 


    else : # col 증가부분
        r, c = row-1, col+1
        while 0<=r<n and 0<=c<n:
            if board[r][c] == 1:
                if y_x_diagonal[r-c+n-1]!=1 :
                    y_x_diagonal[r-c+n-1] = 1
                    bishop(row,col+1,bishop_cnt+1)
                    y_x_diagonal[r-c+n-1] = 0
                    flag = True
            r-=1
            c+=1

        if flag == False: # 사선에 둘 1이 하나도 없었다면
            bishop(row, col+1, bishop_cnt) 


bishop(0,0, 0)
print(ans)