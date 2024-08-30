import sys
sys.setrecursionlimit(20000)

sys.stdin = open('input.txt','r')


input = sys.stdin.readline
# 임의의 정점에서 가장 긴 노드 x와 x에서 가장 긴 정점 y가 있을때 xy가 트리 지름

n = int(input())
graph = [[] for _ in range(n+1)]
ans = -1

for _ in range(n-1):
    a,b,w = map(int,input().split())

    graph[a].append((b, w))
    graph[b].append((a, w))

def dfs(node, w_sum):
    global ans, x_node

    if w_sum > ans:
        ans = w_sum
        x_node = node


    visited[node] = 1
    for adjacent_node, weight in graph[node]:
        if visited[adjacent_node] != 1:
            dfs(adjacent_node, w_sum + weight)
    
    return x_node


visited = [0] * (n+1)
x = dfs(1, 0)

visited = [0] * (n+1)
dfs(x, 0)

print(ans)
