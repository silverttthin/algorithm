import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
edge = int(input())

inf = int(1e9)

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
d = [inf] * (n+1)

for i in range(edge):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start_node, end_node = map(int,input().split())

if start_node == end_node :
    print(0)
    exit()

def get_smallest_node():
    minval = inf
    idx = 0

    for i in range(1, n+1):
        if d[i] < minval and not visited[i]:
            minval = d[i]
            idx = i
    return idx

def dijkstra(start):
    visited[start] = True
    d[start] = 0
    for adj_node, cost in graph[start]:
        d[adj_node] = min(d[adj_node], cost)
    
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for adj_node, cost in graph[now]:
            
            if d[now] + cost < d[adj_node]:
                d[adj_node] = d[now] + cost

dijkstra(start_node)

print(d[end_node])