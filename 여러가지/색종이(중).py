import sys
sys.stdin = open('input.txt','r')

arr= [[0 for i in range(102)] for i in range(102)]

N = int(input())
for _ in range(N):
    x,y = map(int,input().split())

    for i in range(10):
        for j in range(10):
            arr[y+i][x+j] = 1 # 테두리 있는거 감안해서 인덱스조정하기
    
    # 0이라면 인접한 부분이 1이라면 cnt+=1
    cnt = 0
    for i in range(1,101):
        for j in range(1,101):
            if arr[i][j] == 1:
                if arr[i+1][j]==0:cnt+=1
                if arr[i-1][j]==0:cnt+=1
                if arr[i][j-1]==0:cnt+=1
                if arr[i][j+1]==0:cnt+=1
print(cnt)




