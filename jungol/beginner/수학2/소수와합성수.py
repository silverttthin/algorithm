import sys
sys.stdin = open('input.txt', 'r')

arr = list(map(int, input().split()))

# M = max(arr)
# chae = [1 for i in range(M+1)]
# chae[0],chae[1] = 0,0

# for i in range(2, int(M**0.5) + 1):
#     if chae[i] == 1:
#         for j in range(i*i, M+1, i):
#             chae[j] = 0

# sosu = [i for i in range(M+1) if chae[i] == 1]

# for num in arr:
#     if num == 1:
#         print('number one')
#     elif num in sosu:
#         print('prime number')
#     else:
#         print('composite number')
for num in arr:
    if num == 1:
        print('number one')
    else:

        for i in range(2, int(num**0.5)+1):
            if num % i ==0:
                print('composite number')
                break
        else:
            print('prime number')