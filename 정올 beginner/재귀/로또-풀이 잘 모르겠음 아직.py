import sys
sys.stdin = open('input.txt','r')

line = list(map(int,input().split()))

k = line[0]
s = line[1:k+1]

arr = [0 for i in range(7)]
check = [0 for i in range(k+1)]

def lotto(x, tmp):
    if x >6:
        for i in arr[1:]:
            print(i, end=" ")
        print()
        return

    for i in range(tmp, k):
        if check[i] == 1:
            continue
        else:
            arr[x] = s[i]
            check[i]= 1
            lotto(x+1, i+1)
            check[i]= 0


lotto(1, 0)