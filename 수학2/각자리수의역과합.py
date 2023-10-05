import sys
sys.stdin = open('input.txt', 'r')


while 1:
    n = int(input())
    if n == 0:
        break

    n = list(map(int, str(n)))
    n.reverse()

    while 1:
        i = 0
        if n[i]==0:
            n.pop(0)
        else: break

    print(''.join(map(str, n)), sum(n))


