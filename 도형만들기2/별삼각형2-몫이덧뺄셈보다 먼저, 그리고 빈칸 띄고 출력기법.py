import sys
sys.stdin = open('input.txt','r')

# 배열에 채우고 출력하는 방법
# 그리고 어느정도 빈칸을 반복문으로 띄고 나머지 출력하는방법
# 왜냐면 내용물 뒤쪽 빈칸은 무시해도 상관없으니 대칭연연안해도됨

n, m = map(int, input().split())
if n>100 or n%2 ==0 or m<1 or m>4: 
    print("INPUT ERROR!")
    exit()

if m == 1:
    arr= [[0 for i in range((n+1)//2)] for i in range(n)]
    for i in range(n):
        for j in range(i, n-i): # i=0 : i~n-1, i=1: i~n-2
            arr[j][i] = "*"
    
    for i in range(n):
        for j in range((n+1)//2):
            if arr[i][j] == 0 :
                print("", end=" ")
            else:
                print(arr[i][j], end="")
        print()
    
elif m == 2:
    arr= [[0 for i in range((n+1)//2)] for i in range(n)]
    for i in range(n):
        for j in range(i, n-i): # i=0 : i~n-1, i=1: i~n-2
            arr[j][i] = "*"
    
    for i in range(n):
        for j in range((n+1)//2-1, -1, -1):
            if arr[i][j] == 0 :
                print(" ", end="")
            else:
                print(arr[i][j], end="")
        print()

elif m == 3:
    center = (n-1)//2

    # 1. 0 ~ center-1행 까지 채우기
    for i in range(center):
        for blank in range(i):
            print(' ', end="")
        # i줄일 때 n-i*2개
        for star in range(n-i*2):
            print("*", end="")
        print()

    cnt = 1
    # 2. center행 ~ n-1행 까지 채우기
    for i in range(center, n): # 2, 3, 4
        # i행-> n-1-i
        for blank in range(n-1-i):
            print(' ', end="")
        
        for i in range(cnt):
            print('*', end="")
        print()
        cnt += 2

else:
    center = (n-1)//2
    cnt = 1
    for i in range(center):
        for blank in range(i):
            print(' ', end="")
        for star in range(center+1-i):
            print('*', end="")
        print()
    
    for i in range(center, n):
        print(" "*(center),end="")
        for i in range(cnt):
            print("*", end="")
        print()
        cnt += 1
        
