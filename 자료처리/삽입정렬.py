import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

arr= list(map(int, input().split()))

for i in range(1, N):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]: arr[j] , arr[j-1] = arr[j-1], arr[j]
    for elem in arr:
        print(elem, end=" ")
    print()