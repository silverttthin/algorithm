import sys
sys.stdin = open('input.txt', 'r')

bingoArr = []
cnt = 0
bingo_cnt = 0

for _ in range(5):
    bingoArr.append(list(map(int, input().split())))

for _ in range(5):
    call_nums = map(int,input().split())
    for num in call_nums:
        for i in range(5):
            for j in range(5):
                if bingoArr[i][j] == num:
                    bingoArr[i][j] = 0
                    cnt+= 1
                    
                    if bingoArr[i]== [0,0,0,0,0]: 
                        bingo_cnt+= 1
                        if bingo_cnt == 3 :
                            print(cnt)
                            exit()

                    if list(zip(*bingoArr))[j]== (0,0,0,0,0): 
                        bingo_cnt+= 1
                        if bingo_cnt == 3 :
                            print(cnt)
                            exit()
                    
                    if i==j and [bingoArr[0][0],bingoArr[1][1],bingoArr[2][2],bingoArr[3][3],bingoArr[4][4]] == [0,0,0,0,0]:
                        bingo_cnt+= 1
                        if bingo_cnt == 3 :
                            print(cnt)
                            exit()

                    if i+j==4 and [bingoArr[0][4],bingoArr[1][3],bingoArr[2][2],bingoArr[3][1],bingoArr[4][0]] == [0,0,0,0,0]:
                        bingo_cnt+= 1
                        if bingo_cnt == 3 :
                            print(cnt)
                            exit()

                    

