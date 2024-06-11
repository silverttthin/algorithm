import sys;sys.stdin=open('input.txt','r')

# 전위순회 : root left right
# 중위순회 : left root right
# 후위순회 : left right root

N = int(input())
d = {}
for _ in range(N):
    a,b,c = input().split()
    d[a] = [b,c]


def preorder(node):
    # 일단 현 노드 출력 후 왼쪽이 있다면 왼쪽먼저 들어가고 그후 오른쪽
    print(node, end="")
    if d[node][0]!='.':
        preorder(d[node][0])
    if d[node][1]!='.':
        preorder(d[node][1])

def inorder(node):
    if d[node][0]!='.':
        inorder(d[node][0])
    print(node, end="")
    if d[node][1]!='.':
        inorder(d[node][1])    

def postorder(node):
    if d[node][0]!='.':
        postorder(d[node][0])
    if d[node][1]!='.':
        postorder(d[node][1])
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()

