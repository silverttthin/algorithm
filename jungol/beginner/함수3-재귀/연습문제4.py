import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

lst = [0] *n

def dice(x):
    if x == n+1:
        for elem in lst:
            print(elem, end=" ")
        print()
        return 1
    for noon in range(1,6+1):
        lst[x-1]= noon
        dice(x+1)


dice(1)
    
# fx : x번째 주사위의 눈을 결정
# x일 때 x번째 주사위 눈 1부터 6까지 순회해 x-1 인덱스에 담고 출력, 담고 출력을 반복
# 다 출력하면 x ? 1번째 눈을 호출? 

# 이전 눈이 결정된 상태에서 뒷 눈이 1-6을 lst에 넣고 출력해야함