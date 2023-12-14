import sys
sys.setrecursionlimit(10000)


sys.stdin = open('input.txt','r')

n = int(input())

graph = [[] for _ in range(n+1)]
ans = [0 for i in range(n+1)]
visited = ans[:]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visited[node] = 1

    for k in graph[node]:
        if not visited[k]:
            ans[k] = node
            dfs(k)

dfs(1)
for a in ans[2:]:
    print(a)