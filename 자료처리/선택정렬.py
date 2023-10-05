import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

arr = list(map(int, input().split()))

for idx in range(N-1):
    minval= min(arr[idx:])
    minval_idx = arr[idx:].index(minval) + idx
    arr[idx], arr[minval_idx] = minval, arr[idx]

    for val in arr:
        print(val, end=" ")
    print()