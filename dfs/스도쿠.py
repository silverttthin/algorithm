import sys
sys.stdin = open('input.txt','r')


sudoku = [list(map(int,input().split())) for i in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def checking(i,j):
    check = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if sudoku[i][k] in check: check.remove(sudoku[i][k])
        if sudoku[k][j] in check: check.remove(sudoku[k][j])
    
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in check:
                check.remove(sudoku[p][q])

    return check


def dfs(x): # x번째 zero좌표에 유망한 숫자를 넣는 함수
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        exit()

    i, j = zeros[x]
    promising_nums = checking(i,j)
    
    for num in promising_nums:
        sudoku[i][j] = num
        dfs(x+1)
        sudoku[i][j] = 0


dfs(0)