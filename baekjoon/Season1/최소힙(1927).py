import sys

# 타임아웃 코드
sys.stdin = open("input.txt",'r')

n = int(input())

arr = []

def heapify(arr,n,i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l<n and arr[smallest] > arr[l]:
        smallest = l
    if r<n and arr[smallest] > arr[r]:
        smallest = r
    
    if smallest!= i: 
        arr[i],arr[smallest] = arr[smallest], arr[i]
        heapify(arr,n,smallest) 
        # 위 노드가 내려왔다면 내려온 노드가 자식들과 힙 형태일거란 보장 없으니
        # 한번더 heapify 수행


# 정수가 들어오면 배열에 추가
# 0이 들어오면 최소힙형태로 만들어서
# 루트를 pop하고 힙 속성유지
    
for _ in range(n):
    x = int(input())
    if x == 0 and arr == []:
        print(0)
    elif x>0 :
        arr.append(x)
    else :
        n = len(arr)
        for i in range(n//2-1,-1,-1): # 힙으로만들고
            heapify(arr,n,i)
        print(arr.pop(0))
        for i in range(n-1,0,-1):
            heapify(arr,i,0)
    
