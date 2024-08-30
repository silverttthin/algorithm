import sys;sys.stdin=open('input.txt','r')

N = int(input())
tree = list(map(int, input().split()))
del_node = int(input())


def dfs(node):
    tree[node] = -2
    for i in range(N):
        if tree[i] == node:
            dfs(i)

dfs(del_node)

cnt = 0
for i in range(N):
    if tree[i]!=-2 and i not in tree:
        cnt+=1

print(cnt)