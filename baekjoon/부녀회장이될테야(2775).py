import sys;sys.stdin=open('input.txt','r')

# k층 n호 = k층 n-1호 + k-1층 n호
apartment = [[0] * 15 for _ in range(15)] # 호실은 1호시작
for i in range(1, 15): # 0층 base만들기
    apartment[0][i] = i

for i in range(1, 14+1):
    for j in range(1, 14+1):
        apartment[i][j] = apartment[i][j-1] + apartment[i-1][j]

T = int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    print(apartment[k][n])
