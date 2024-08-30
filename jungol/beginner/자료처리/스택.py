import sys
sys.stdin = open('input.txt','r')

N = int(input())

stack = []

for _ in range(N):
    line = input().split()
    if line[0] == 'i':
        stack.append(line[1])
    elif line[0] == 'o':
        if stack == []:
            print('empty')
        else:
            print(stack.pop())
    
    else:
        print(len(stack))