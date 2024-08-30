import sys
sys.setrecursionlimit(1000000)


sys.stdin = open('input.txt','r')

T = int(input())
def dfs(node, color):
    visited[node] = color

    for adjacent_node in graph[node]:
        if visited[adjacent_node] == 0:
            tmp = dfs(adjacent_node, -color)   

            if tmp == -1:
                return -1
        else:
            if visited[adjacent_node] == color: # 방문했던 인접 노드 색이 현 노드 색과 같다면 이분그래프 탈락
                return -1
    return 1


for _ in range(T):
    node, edge = map(int,input().split())
    graph = [[] for _ in range(node+1)]
    visited = [0] * (node+1)
    for _ in range(edge):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    

    for i in range(1, node+1):
        if visited[i] == 0:
            tmp = dfs(i,1)

            if tmp == -1:
                break
    
    if tmp == -1 : print('NO')
    else: print('YES')

