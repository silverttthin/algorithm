import sys;sys.stdin=open('input.txt','r')

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2]) # i번째 집을 어떤색으로 칠하는 비용 = 해당비용 + 다른색들로 이전집을 칠한 비용 중 min
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][1], arr[i-1][0])

# 0번째 집을 제외한 각 집에 대해서, 
# 이전 집을 다른 색으로 칠하는 데 드는 최소 비용을 재사용해
# 현재 집을 해당 색으로 칠하는 비용을 더해 arr를 갱신
# 이렇게 해서 각 색깔별로 최소 비용을 계속 갱신해 나갑니다.
print(min(arr[n-1]))