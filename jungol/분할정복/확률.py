import sys
sys.stdin= open('input.txt','r')

# x번 던져서 y번 나올 확률은 y * 100 / x를 내림한 값인 z이다.
x,y = map(int,input().split())
original_z = y * 100 // x
ans = 0
left, right = 0, 200

ans = -1
while left<=right:
    mid = (left+right)//2
    z = (y+mid) * 100 // ( x+mid)
    if  z> original_z:
        ans = mid
        right = mid -1
    else:
        left = mid + 1

print(ans)

