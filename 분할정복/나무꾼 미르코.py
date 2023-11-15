import sys
sys.stdin= open('input.txt','r')

n, m = map(int,input().split())
heights = list(map(int,input().split()))
# m미터 이상의 나무를 벌목해야 할 때 절단기 최대높이를 구하라
harvest = 0
def binSearch(left, right):
    if left > right :
        return right
    harvest = 0
    mid = (left + right) // 2
    for height in heights:
        tmp = height - mid
        if tmp < 0 : tmp = 0
        harvest += tmp

    if harvest == m : return mid
    elif harvest > m : return binSearch(mid+1, right)
    else: return binSearch(left, mid-1)

_min = min(heights)
for height in heights:
    tmp = height - _min
    if tmp < 0 : tmp = 0
    harvest += tmp

if harvest < m : print(binSearch(0, _min))
elif m < harvest : print(binSearch(_min, max(heights)))
else: print(_min)