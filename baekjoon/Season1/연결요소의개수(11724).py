import sys
sys.setrecursionlimit(10000)

sys.stdin = open('input.txt','r')

vertex, edge = map(int,input().split())
graph = [[] for _ in range(vertex+1)]
visited = [0 for _ in range(vertex + 1)]

def dfs(node):
    visited[node] = 1
    for j in graph[node]:
        if visited[j] != 1:
            dfs(j)
    return
connected_component = 0
for _ in range(edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



for i in range(1,vertex+1):
    if visited[i] != 1:
        dfs(i)
        connected_component+=1

print(connected_component)






