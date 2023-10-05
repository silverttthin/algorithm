import sys
import math
sys.stdin = open('input.txt', 'r')

N = int(input())

chae = [1 for i in range(2*1000000+2)]
chae[0], chae[1]= 0, 0


for i in range(2, int(math.sqrt(2*1000000+2))): 
    for j in range(i*i, 2*1000000+2, i): 
        if chae[j] ==1 : chae[j]= 0


for i in range(N):
    m = int(input())
    # m번째 인덱스부터 좌우로 시작해서 먼저 1이 뜨는 것의 인덱스를 리턴
    # 근데 동시에 1이 뜨면 둘다 출력
    l,r = m,m
    while 1:
        if (chae[l]==1 or chae[r]== 1) and l!=r:
            if chae[l] == 1 and chae[r] == 1: 
                print(l, r)
                break
            elif chae[r] == 1: 
                print(r)
                break
            else : 
                print(l)
                break

        elif (chae[l]==1 and chae[r]==1) and l==r: 
            print(m)
            break

        else:
            l-=1
            r+=1
        
        
