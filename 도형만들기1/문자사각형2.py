import sys

sys.stdin = open('input.txt','r')

n = int(input())
chars = [chr(i) for i in range(65, 91)]

array = [[0 for _ in range(n)] for _ in range(n)]

k = 0
for i in range(n):
    for j in range(n):
        array[i][j] = chars[k]
        k +=1
        if k >= 26: k = 0

for row in range(n):
    if row % 2 !=0 :
        array[row][:] = array[row][::-1]


for i in range(n):
    for j in range(n):
        print(array[j][i], end= " ")
    print()