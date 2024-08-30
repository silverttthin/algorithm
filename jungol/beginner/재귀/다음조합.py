import sys
sys.stdin = open('input.txt','r')

n, k = map(int,input().split())
tmp = list(map(int, input().split()))

flag = 0
tmp_comb = [0 for i in range(k+1)]

def combination(level):
    global flag
    if level > k:
        if flag == 1:
            for val in tmp_comb[1:]:
                print(val, end=" ")
            exit()

        if tmp == tmp_comb[1:]:
            flag = 1
        return

    for i in range(1, n+1):
        if i <= tmp_comb[level-1]:
            continue

        else:
            tmp_comb[level] = i
            combination(level+1)
    
combination(1)
print("NONE")