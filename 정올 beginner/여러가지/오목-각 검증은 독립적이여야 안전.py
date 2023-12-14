import sys
sys.stdin = open('input.txt','r')

board = [list(map(int, input().split())) for i in range(19)]

def garo_check(i, j, color):
    original_i, original_j = i, j
    cnt = 0

    # 가로 체크
    if board[i][j-1] == color and j != 0 : 
        return # 이전치와 같다면 체크필요없음

    if j>=15: return 
    else:
        try: # 오목 이상이 인덱스 넘어갈때까지 있을 경우 대비
            while board[i][j] == color: 
                cnt+=1     
                j+=1
        except: pass

        if cnt == 5: 
            print(f'{color}\n{original_i + 1} {original_j + 1}')
            exit()


def sero_check(i,j,color):
    original_i, original_j = i, j
    cnt = 0
    # 세로 체크
    if board[i-1][j] == color and i != 0 : 
        return # 이전치와 같다면 체크필요없음

    if i>=15: return 
    else:
        try: # 오목 이상이 인덱스 넘어갈때까지 있을 경우 대비
            while board[i][j] == color: 
                cnt+=1     
                i+=1
        except: pass

        if cnt == 5:
            print(f'{color}\n{original_i + 1} {original_j + 1}')
            exit()


def diagonal_check_1(i,j,color):
    original_i, original_j = i, j
    cnt = 0

    # y=-x 체크
    if board[i-1][j-1] == color and i != 0 and j != 0: 
        return # 이전치와 같다면 체크필요없음

    if i>=15 or j >=15: return 
    else:
        try: # 오목 이상이 인덱스 넘어갈때까지 있을 경우 대비
            while board[i][j] == color: 
                cnt+=1     
                i+=1
                j+=1
        except: pass

        if cnt == 5:
            print(f'{color}\n{original_i + 1} {original_j + 1}')
            exit()
    
    i = original_i
    j = original_j
    cnt = 0

def diagonal_check_2(i,j,color):
    original_i, original_j = i, j
    cnt = 0

    # y=+x 체크
    if board[i-1][j-1] == color and i != 0 and j != 0: 
        return # 이전치와 같다면 체크필요없음

    if i<=3 or j >=15: return 
    else:
        try: # 오목 이상이 인덱스 넘어갈때까지 있을 경우 대비
            while board[i][j] == color: 
                cnt+=1     
                i-=1
                j+=1
        except: pass

        if cnt == 5:
            print(f'{color}\n{original_i + 1} {original_j + 1}')
            exit()

for i in range(18):
    for j in range(18):                
        if board[i][j] != 0:
            garo_check(i, j, board[i][j])
            sero_check(i, j, board[i][j])
            diagonal_check_1(i, j, board[i][j])
            diagonal_check_2(i, j, board[i][j])

print(0)