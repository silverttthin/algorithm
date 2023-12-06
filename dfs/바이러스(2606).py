import sys
sys.stdin = open('input.txt','r')

vertex = int(input())
edge = int(input())
adj_list = [[] for i in range(vertex+1)]
check = [0 for i in range(vertex+1)]

for i in range(edge):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 1번 리스트에서 들어갈 수 있는 것을 찾아봄
# 들어갔으면 체크배열에 체크하고 cnt 증가
# 체크배열에 들어가 있는 것은 무시하고 계속해서 찾아봄

def dfs(n):
    global check
    check[n] = 1

    for i in adj_list[n]:
        if check[i] != 1:
            dfs(i)
    return

dfs(1)
print(sum(check)-1)