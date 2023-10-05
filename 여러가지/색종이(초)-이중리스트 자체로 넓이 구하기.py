import sys
sys.stdin = open('input.txt','r')

T = int(input())

cnt = 0
cPapers =[]
for _ in range(T):
    cPapers.append(tuple(map(int, input().split())))

# 0으로 초기화한 100 * 100 리스트 만들기
# 좌표 지점으로부터 +10 * +10 영역을 0이라면 1로 채우기
# 리스트에서 1인 부분의 개수 리턴

lst = [[0 for _ in range(100)] for _ in range(100)]   

for y,x in cPapers:
    for i in range(10):
        for j in range(10): 
            if lst[x-1+i][y-1+j] ==0: lst[x-1+i][y-1+j] = 1

for row in range(100):
    for col in range(100):
        if lst[row][col] == 1 : cnt +=1

print(cnt)
