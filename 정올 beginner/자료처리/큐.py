import sys
sys.stdin = open('input.txt','r')

N = int(input())

q = []

for _ in range(N):
    line = input().split()
    if line[0] == 'i':
        q.append(line[1])
    elif line[0] == 'o':
        if q == []:
            print('empty')
        else:
            print(q.pop(0))
    
    else:
        print(len(q))