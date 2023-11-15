import sys
sys.stdin = open('input.txt','r')

row, col = map(int,input().split())

papers = int(input())
error_square_cnt = int(input())
error_squares = [list(map(int,input().split())) for _ in range(error_square_cnt)]
error_squares.sort(key=lambda x:x[1])
# 가리는데 필요한 최소한의 색종이 개수 구하기

# 1. 색종이 길이를 n으로 정한다
# 2. 얼룩이 나오면 x+n ^2만큼의 영역의 얼룩을 모두 가린다 + 색종이카운트 증가
# 3. 그다음 얼룩이 나오면 2를 반복한다.


def checker(n): # 색종이 길이가 n개일 때 필요한 색종이 개수 리턴하는 함수
    demanding_paper_cnt = 1
    width_range = error_squares[0][1] + n-1

    for y, x in error_squares[1:]:
        if x > width_range:
            demanding_paper_cnt += 1
            width_range = x+n-1


    return demanding_paper_cnt


left, right = max(error_squares, key=lambda x:x[0])[0], 10000
while left <= right:
    mid = (left+right)//2

    tmp = checker(mid)
    if tmp<=papers:
        ans = mid
        right = mid -1
    elif tmp>papers:
        left = mid+1

print(ans)



