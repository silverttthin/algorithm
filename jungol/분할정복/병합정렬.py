import sys
sys.stdin = open('input.txt','r')

n = int(input())
lst = list(map(int,input().split()))

def mergeSort(left,right):
    b= []

    if left >= right:
        return
    
    mid = (left+right) // 2

    mergeSort(left, mid)
    mergeSort(mid+1, right)

    i = left
    j = mid+1
    while i<=mid and j<=right:
        if lst[i]<=lst[j]:
            b.append(lst[i])
            i+=1
        else:
            b.append(lst[j])
            j+=1

    for k in range(i, mid+1):
        b.append(lst[k])
    for k in range(j, right+1):
        b.append(lst[k])


    for i in range(left, right+1):
        lst[i] = b[i-left]
    for i in range(n):
        print(lst[i], end= " ")
    print()

mergeSort(0, n-1)