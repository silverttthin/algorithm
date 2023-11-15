import sys
sys.stdin = open('input.txt','r')


n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = list(map(int,input().split()))

def binSearch(left,right,target):
    if right<left : return -1
    mid = (left+right)//2
    
    if a[mid] == target: return mid
    elif a[mid] < target: return binSearch(mid+1, right,target)
    else: return binSearch(left, mid-1, target)

for i in b:
    print(binSearch(0,n-1, i),end=" ")