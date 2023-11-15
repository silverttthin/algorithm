import sys
sys.stdin = open('input.txt','r')
n = int(input())
lst = list(map(int,input().split()))


def quickSort(left, right):
    if left>=right:
        return
    
    pivot = lst[right]
    l = left
    for i in range(left, right):
        if lst[i] < pivot :
            lst[i], lst[l] = lst[l], lst[i]
            l +=1
    
    lst[right], lst[l] = lst[l], lst[right]
    
    for elem in lst:
        print(elem, end=" ")
    print()

    quickSort(left, l-1)
    quickSort(l+1, right)
    

quickSort(0, n-1)

