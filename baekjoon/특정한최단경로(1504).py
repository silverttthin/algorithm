import sys

sys.stdin = open('input.txt','r')

input = sys.stdin.readline
vertex, edge = map(int,input().split())

inf = int(1e9)
graph = [[inf] * (vertex + 1) for _ in range(vertex + 1)]

for i in range(1,vertex+1):
    graph[i][i] = 0

for _ in range(edge):
    a,b,cost = map(int,input().split())
    graph[a][b] = min(graph[a][b], cost)
    graph[b][a] = graph[a][b]

t1,t2 = map(int,input().split())

for k in range(1,vertex+1):
    for a in range(1,vertex+1):
        if k == a : continue
        for b in range(1, vertex+1):
            if b==k or b==a : continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            graph[b][a] = graph[a][b]

# 1 t1 t2 n
t1_t2_path = graph[1][t1] + graph[t1][t2] + graph[t2][vertex]
# 1 t2 t1 n
t2_t1_path = graph[1][t2] + graph[t2][t1] + graph[t1][vertex]

ans = min(t1_t2_path,t2_t1_path)

if ans == inf:
    print(-1)
else:
    print(ans)