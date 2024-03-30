import sys
sys.stdin = open('input.txt','r')

# 무조건 length안에서 좌표처리해야한다 생각했음
# 상대적으로 위치만 옮겨지는거라 길이는 절대적임. r-l은 10-num이나 24-num`이나 같을거임

length = int(input())
arr = [list(map(int,input().split())) for _ in range(3)]
l,r = 0, length

def u(m, n) : return m + abs(n-m) 
# n이 접히는 지점서 우방향으로

for i in range(3):
    if arr[i][0] == arr[i][1]: continue

    mid = (arr[i][0] + arr[i][1]) / 2

    # 무조건적으로 일단 기준점기준 오른방향으로 접어봄
    for j in range(i,3): 
        arr[j][0] = u(mid, arr[j][0])
        arr[j][1] = u(mid, arr[j][1])

    l = u(mid,l) 
    # 그러면 점들좌표, l은 mid에서 우측으로 +abs(mid-l)만큼 증가

    if l > r: # r을 넘어섰다면 이 케이스는 왼쪽방향으로 접어야 된단 의미
        r = l
    l = mid

ans = r-l
print("%.1f" %ans)

